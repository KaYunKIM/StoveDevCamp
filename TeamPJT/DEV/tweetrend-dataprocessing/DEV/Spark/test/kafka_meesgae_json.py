import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext, functions
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.types import Row
import json

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=10.250.93.207:9042 pyspark-shell'


if __name__=="__main__":
    def handle_rdd(rdd):
        if not rdd.isEmpty():
            global ss
            dataframe = ss.createDataFrame(rdd, schema = ['data', 'includes', 'matching_rules'])
            newdf = dataframe.withColumn("jsonCol", functions.to_json(functions.struct([dataframe[x] for x in dataframe.columns])))

            #newdfdf = [Row.asDict() for row in newdf.select('jsonCol').collect()]
                    #select('jsonCol').take(1)]
            newdf_to_json = newdf.select('jsonCol').collect()[0].asDict()
            print(newdfdf)
            print('type of newdfdf[jsonCol]', type(newdfdf['jsonCol']))
            newdf_value_to_json = json.loads(newdfdf['jsonCol'])


           # df = dataframe.
           # dataframe.write \
            #    .format("org.apache.spark.sql.cassandra") \
             #   .mode('append') \
              #  .options(table="words", keyspace="streaming_test") \
               # .save()
                # .saveAsTable(name="words")

    sc = SparkContext(appName="Kafka Spark Demo")
    ssc = StreamingContext(sc,5)  #5=no.of seconds
    ss = SparkSession.builder \
        .appName('SparkCassandraApp') \
        .config('spark.cassandra.connection.host', '10.250.93.207') \
        .config('spark.cassandra.connection.port', '9042') \
        .config('spark.cassandra.output.consistency.level', 'ONE') \
        .getOrCreate()

    message = KafkaUtils.createDirectStream(ssc, topics=["test"],
                kafkaParams={"metadata.broker.list":"10.250.93.4:9092"})

    message = message.map(lambda x: json.loads(x[1]))
    message = message.map(lambda tweet: json.loads(tweet))

   # message.pprint()
    message.foreachRDD(handle_rdd)

    ssc.start()
    ssc.awaitTermination()
