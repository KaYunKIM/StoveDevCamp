import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

#Cassandra
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=localhost pyspark-shell'

# com.datastax.spark.connector.streaming._

if __name__=="__main__":
    def handle_rdd(rdd):
        if not rdd.isEmpty():
            global ss
            dataframe = ss.createDataFrame(rdd, schema=['word', 'count'])
            dataframe.show(5)
            dataframe.write \
                .format("org.apache.spark.sql.cassandra") \
                .mode('append') \
                .options(table="words", keyspace="streaming_test") \
                .save()
                # .saveAsTable(name="words")

    sc = SparkContext(appName="KafkaSparkApp")
    ssc = StreamingContext(sc,5)  #5=no.of seconds
    ss = SparkSession.builder \
        .appName('SparkCassandraApp') \
        .config('spark.cassandra.connection.host', 'localhost') \
        .config('spark.cassandra.connection.port', '9042') \
        .config('spark.cassandra.output.consistency.level', 'ONE') \
        .getOrCreate()

    message = KafkaUtils.createDirectStream(ssc, topics=["test"],
                kafkaParams={"metadata.broker.list":"localhost :9092"})

    message.pprint()
    # words = message.map(lambda x: x[1]).flatMap(lambda x: x.split(" "))
    # wordcount = words.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b)
    # wordcount.pprint()

    lines = message.map(lambda x: x[1])
    transform = lines.map(lambda tweet: (tweet, int(len(tweet.split()))))
    transform.foreachRDD(handle_rdd)

    # Cassandra keyspace = "streaming_test, table name = "words"
    # wordcount.saveToCassandra("streaming_test", "words", SomeColumns("word","count"))

    # sqlctx = SQLContext(sc)
    # df = sqlctx.createDataFrame(wordcount)
    # df.show(5)

    # rdd = wordcount.cassandraTable("Streaming_test", "key_value").select("key", "value").where("fu=?", 3)
    # dataframe = ss.createDataFrame(rdd, schema=['words', 'count'])
    # dataframe.show(5)

    # dataframe.write \
    #     .format("org.apache.spark.sql.cassandra") \
    #     .mode('append') \
    #     .options(keyspace="streaming_test", table="words") \
    #     .saveAsTable(name="words")
    #     .save()

    ssc.start()
    ssc.awaitTermination()