import Schema, list_reshape

import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from datetime import datetime
#import pandas as pd
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

            def has_column(df,col):
                try:
                    df[col]
                    return True
                except:
                    return False

            # dataframe = ss.createDataFrame(rdd)
            # dataframe.show(3)

            df = ss.createDataFrame(rdd, Schema.tweet_data)
            # df.show(3)

            new_df = df.toJSON().map(lambda x: json.loads(x)).collect()
            #print('new_df', type(new_df[0]), new_df)
            #print()
            
            json_return = list_reshape.reshape(new_df,'covid-19')   # json_list, topic
            
            # convert list to RDD
            dataframe = sc.parallelize(json_return).map(lambda x: json.dumps(x))
            dataframe = ss.read.json(dataframe)

            print('dataframe', type(dataframe), dataframe)
            
            #dataframe = ss.read.json(sc.parallelize(json_return))     
            #dataframe_return = dataframe.select('_corrupt_record').collect()
            #print('dataframe_return', dataframe_return[0]['_corrupt_record'])   # list type


            # "includes"
            # if has_column(dataframe['includes'], 'tweets'):
            #     includes = dataframe.select('includes').collect()
            #     for tweet in row['includes']['tweets']:
            #         if 'entities' in tweet and 'urls' in tweet['entities']:
            #             tweet['text'], tweet['entities']['urls'] = reform_message(tweet['text'], tweet['entities']['urls'])

            #     if 'media' in row['includes']:
            #         for medium in row['includes']['media']:
            #             if 'public_metrics' in medium:
            #                 medium['view_count'] = medium['public_metrics']['view_count']

            #                 del medium['public_metrics']

            
            # "data"
            #tweet_data = dataframe.select('data').collect()
            #print(tweet_data)
            # print(has_column(tweet_data, 'referenced_tweets'))
            # if has_column(dataframe['data'], 'referenced_tweets'):
            #     rf_tweets = dataframe.select('data').collect()
            #     print(type(rf_tweets), rf_tweets)
            #     for rf in rf_tweets:
            #         print('before', type(rf[0][0]), rf[0][0])
            #         rf[0][0]['id'] = int(rf[0][0]['id'])
            #         print('after', type(rf[0][0]['id']), rf[0][0]['id'])
            #         print()
            

            # new_df = dataframe.toPandas()
            # print(reshape(new_df, '코로나'))

            # data_json = {}
            # includes_json = {}
            #
            # new_df = dataframe.toJSON().map(lambda x: json.loads(x)).collect()
            # for i in new_df:
            #     data_json['data'] = i['data']
            #     includes_json['includes'] = i['includes']

            # data_json['data']['id'] = int(data_json['data']['id'])
            # print(bin['data']['id'], type(bin['data']['id']))

            # print(data_json['data']['entities'])
            # print(includes_json.items())
            

            dataframe.write \
                .format("org.apache.spark.sql.cassandra") \
                .mode('append') \
                .options(table="tweets", keyspace="tweetrend") \
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

    message_data = message.map(lambda tweet: tweet['data'])

    # referenced_tweets_type = message_data.map(
    #     lambda data: data['referenced_tweets'][0]['type'] if data['referenced_tweets'] else None)
    # referenced_tweets_id = message_data.map(
    #     lambda data: int(data['referenced_tweets'][0]['id']) if data['referenced_tweets'] else None)
    #
    # print(type(referenced_tweets_type), type(referenced_tweets_id))

    # referenced_tweets_id = message.map(
    #     lambda tweet: int(tweet['data']['referenced_tweets'][0]['id']) if tweet['data']['referenced_tweets'] else None)

    # message_data = message_data.map(lambda data: data['referenced_tweets'].update({
    #     'type': data['referenced_tweets']['type'],
    #     'id': int(data['referenced_tweets']['id'])})
    #      if data['referenced_tweets'] else None)
    #
    # message_data.pprint()

    # referenced_tweets = {}
    # referenced_tweets["type"] = referenced_tweets_type
    # referenced_tweets["id"] = referenced_tweets_id
    #
    # message = message.map(lambda x: x)
    # message_data_referenced_tweets.pprint()

    # referenced_tweets = message_data.map(lambda data: data['referenced_tweets']  )
    # referenced_tweets = message_data.map(lambda data: json.loads(data['referenced_tweets'][0]) if data['referenced_tweets'] else None)
    # referenced_tweets.pprint()

    # message_data_referenced_tweets.pprint()
    # type(message_data_referenced_tweets["id"]).pprint()
    # message_data_referenced_tweets["id"].pprint()


    # message_includes = message.map(lambda tweet: tweet['includes'])

    message.foreachRDD(handle_rdd)
    # message.pprint()

    ssc.start()
    ssc.awaitTermination()
