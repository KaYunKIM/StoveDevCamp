import Schema, reshape

import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from datetime import datetime
import json

## Cassandra
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=10.250.93.207:9042 pyspark-shell'

if __name__=="__main__":
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def handle_rdd(rdd):
        if not rdd.isEmpty():
            global ss, now
            
            data_in = "data_in.txt"
            data_out = "data_out.txt"

            def has_column(df,col):
                try:
                    df[col]
                    return True
                except:
                    return False
            
            dataframe = ss.createDataFrame(rdd, Schema.tweet_data)
            
            ## data_in count test
            with open(data_in, "a") as di:
                di.write(now)
                di.write(str(dataframe.count()))

            ## remove 'matchin_rules' column
            dataframe = dataframe.drop('matching_rules')
            #dataframe.show(3)
            
            ## dataframe to JSON(list)
            df = dataframe.toJSON().map(lambda x: json.loads(x)).collect()
            
            ## JSON reshape return
            reshaped_json = reshape.reshape(df,'covid-19')   ## json(list), topic
            
            ## convert list to RDD
            new_df = sc.parallelize(reshaped_json).map(lambda x: json.dumps(x))

            ## convert RDD to Dataframe
            new_df = ss.read.json(new_df)

            #print('new_df', type(new_df), new_df)
            new_df.show(3)
            print()
            
            ## data_out count test
            with open(data_out, "a") as do:
                do.write(now)
                do.write(str(dataframe.count()))

            output_file_name = "error_message.txt"

            try: 
                new_df.write \
                    .format("org.apache.spark.sql.cassandra") \
                    .mode('append') \
                    .options(table="tweets", keyspace="tweetrend") \
                    .save()

            except Exception as e:
                with open(output_file_name, "a", encoding="utf-8") as output_file:
                    output_file.write(type(e), e)
                    output_file.write(reshaped_json)


    sc = SparkContext(appName="Kafka Spark Demo")
    ssc = StreamingContext(sc,5)  ## 5 = no.of seconds
    ss = SparkSession.builder \
        .appName('SparkCassandraApp') \
        .config('spark.cassandra.connection.host', '10.250.93.207') \
        .config('spark.cassandra.connection.port', '9042') \
        .config('spark.cassandra.output.consistency.level', 'ONE') \
        .getOrCreate()

    message = KafkaUtils.createDirectStream(ssc, topics=["test"],
                kafkaParams={"metadata.broker.list":"10.250.93.4:9092"})

    message = message.map(lambda x: json.loads(x[1]))
    message.foreachRDD(handle_rdd)
    # message.pprint()

    ssc.start()
    ssc.awaitTermination()