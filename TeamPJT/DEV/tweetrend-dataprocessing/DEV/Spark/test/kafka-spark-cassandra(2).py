import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

#Cassandra
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=10.250.93.207:9042 pyspark-shell'


if __name__=="__main__":
    def handle_rdd(rdd):
        if not rdd.isEmpty():
            global ss
            dataframe = ss.createDataFrame(rdd, schema=["text", "id", "created_at"])
            dataframe.show(5)
            print(dataframe.count())
            dataframe.write \
               .format("org.apache.spark.sql.cassandra") \
               .mode('append') \
               .options(table="test_tweets", keyspace="tweetrend_test") \
               .save()

    sc = SparkContext(appName="Kafka Spark Demo")
    ssc = StreamingContext(sc,5)  #5 = no.of seconds
    ss = SparkSession.builder \
        .appName('SparkCassandraApp') \
        .config('spark.cassandra.connection.host', '10.250.93.207') \
        .config('spark.cassandra.connection.port', '9042') \
        .config('spark.cassandra.output.consistency.level', 'ONE') \
        .getOrCreate()

    message = KafkaUtils.createDirectStream(ssc, topics=["test"],
                kafkaParams={"metadata.broker.list":"10.250.93.4:9092"})

    
    message = message.map(lambda x: json.loads(x[1]))
    message = message.map(lambda x: json.loads(x))

    message = message.map(lambda tweet: (tweet['data']['text'], tweet['data']['id'], tweet['data']['created_at']))
    message.foreachRDD(handle_rdd)
    # message.pprint()

    ssc.start()
    ssc.awaitTermination()