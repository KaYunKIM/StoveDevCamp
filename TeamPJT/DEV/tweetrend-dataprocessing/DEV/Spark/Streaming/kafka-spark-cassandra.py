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
    ' --conf spark.cassandra.connection.host=localhost:port pyspark-shell'

if __name__=="__main__":
    cnt_in = 0
    cnt_out = 0
    
    def handle_rdd(rdd):
        global ss, now, cnt_in, cnt_out

        if not rdd.isEmpty():
            
            data_in = "data_in.txt"
            data_out = "data_out.txt"

            def has_column(df,col):
                try:
                    df[col]
                    return True
                except:
                    return False
            
            dataframe = ss.createDataFrame(rdd, Schema.tweet_data)
            
            ## data_in count
            with open(data_in, "a") as di:
                cnt_in+= dataframe.count()
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                di.write(now + '\n')
                di.write('per 5 seconds: '+ str(dataframe.count()) +'  total count: ' + str(cnt_in) + '\n')

            ## remove 'matchin_rules' column
            dataframe = dataframe.drop('matching_rules')
            #dataframe.show(3)
            
            ## dataframe to JSON(list)
            df = dataframe.toJSON().map(lambda x: json.loads(x)).collect()
            
            ## JSON reshape return
            reshaped_json = reshape.reshape(df,'covid-19')   ## json(list), topic
            
            ## convert list to RDD to Json
            new_df = sc.parallelize(reshaped_json).map(lambda x: json.dumps(x))

            ## convert Json to Dataframe
            new_df = ss.read.json(new_df)

            new_df.show(3)
            print()
            
            ## data_out count
            with open(data_out, "a") as do:
                cnt_out+=new_df.count()
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                do.write(now + '\n')
                do.write('per 5 seconds: ' + str(new_df.count()) + '  total count: ' + str(cnt_out) + '\n')

            output_file_name = "error_message.txt"

            try: 
                new_df.write \
                    .format("org.apache.spark.sql.cassandra") \
                    .mode('append') \
                    .options(table="tweets", keyspace="tweettrend") \
                    .save()

            except Exception as e:
                with open(output_file_name, "a", encoding="utf-8") as output_file:
                    output_file.write(type(e), e)
                    output_file.write(reshaped_json)


    sc = SparkContext(appName="BigSmile")
    ssc = StreamingContext(sc,5)  ## 5 = no.of seconds
    ss = SparkSession.builder \
        .appName('SparkCassandraApp') \
        .config('spark.cassandra.connection.host', 'localhost') \
        .config('spark.cassandra.connection.port', 'port') \
        .config('spark.cassandra.output.consistency.level', 'ONE') \
        .getOrCreate()

    message = KafkaUtils.createDirectStream(ssc, topics=["covid_kor"],
                kafkaParams={"metadata.broker.list":"localhost:port"})

    try: 
        message = message.map(lambda x: json.loads(x[1]))
        ## each tweet data to RDD
        message.foreachRDD(handle_rdd)

    except Exception as e:
        with open(data_in, "a") as di:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            di.write(now + '\n')
            di.write(type(e), e)

    ssc.start()
    ssc.awaitTermination()
