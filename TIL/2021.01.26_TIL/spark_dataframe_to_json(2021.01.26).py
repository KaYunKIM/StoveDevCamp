import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from datetime import datetime
import pandas as pd
import json

#Cassandra
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=10.250.93.207:9042 pyspark-shell'


if __name__=="__main__":
    
    # cassandra_reshape
    # def reform_message(message, urls):
    #     '''
    #     :param message: str, tweet->text
    #     :param urls: str, entities->urls
    #     :return: (str, urls), new message with expanded url and new urls with filtering
    #     '''
    #     for url in urls:
    #         new_msg = message[:url['start'] - 1] + url['expanded_url'] if url['start'] > 0 else url['expanded_url']
    #         new_msg = new_msg + message[url['end']:] if url['end'] < len(message) else new_msg
    #
    #         for key in list(set(['status', 'title', 'description', 'images']) & set(url.keys())):
    #             del url[key]
    #
    #     return new_msg, urls
    #
    #
    # def reshape(dataframe, topic):
    #     '''
    #     :param dataframe: dataframe, a set of data, includes, and matching_rules
    #     :param topic: str, topic of the json_file
    #     :return: dataframe, reshaped data for insert into tweets
    #     '''
    #
    #     json_file = json.loads(dataframe.to_json(orient='table'))
    #
    #     print(json_file)
    #
    #     row = json_file['data'][0]['data'].copy()
    #
    #     if 'includes' in json_file['data'][0]:
    #         # print(type(row), row)
    #         row['includes'] = json_file['data'][0]['includes']
    #         if 'tweets' in row['includes']:
    #             for tweet in row['includes']['tweets']:
    #                 if 'entities' in tweet and 'urls' in tweet['entities']:
    #                     tweet['text'], tweet['entities']['urls'] = reform_message(tweet['text'],
    #                                                                               tweet['entities']['urls'])
    #
    #         if 'media' in row['includes']:
    #             for medium in row['includes']['media']:
    #                 if 'public_metrics' in medium:
    #                     medium['view_count'] = medium['public_metrics']['view_count']
    #                     del medium['public_metrics']
    #     # print(type(row), row)
    #
    #     row['id'] = int(row['id'])
    #
    #     row['topic'] = topic
    #
    #     if 'referenced_tweets' in row and row['referenced_tweets'][0]['type'] == 'retweeted':
    #         row['text'] = row['includes']['tweets'][0]['text']
    #
    #     elif 'entities' in row and 'urls' in row['entities']:
    #         row['text'], row['entities']['urls'] = reform_message(row['text'], row['entities']['urls'])
    #
    #     if 'geo' in row:
    #         row['place_id'] = row['geo']['place_id']
    #
    #         del row['geo']
    #
    #     created_at = row['created_at'].split('T')
    #     row['datehour'] = -int(''.join(created_at[0].split('-')[1:]) + ''.join(created_at[1].split(':')[:2]))
    #     # print(created_at, row['datehour'])
    #
    #     row['stored_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #
    #     result = json.loads(json.dumps(row).replace('\"text\":', '\"message\":'))
    #
    #     return pd.DataFrame(data=[result.values()], columns=list(result.keys()))

    
    def handle_rdd(rdd):
        if not rdd.isEmpty():
            global ss
            dataframe = ss.createDataFrame(rdd)
            dataframe.show(3)

            bin = {}
            # new_df = dataframe.select('referenced_tweets').collect()
            # new_df_df = new_df[0]
            referenced_tweets_df = dataframe.columns.contains('referenced_tweets')
            print(referenced_tweets_df)
            if referenced_tweets_df:
                print('yessss')
            else:
                print('faillll')

            # print(new_df, new_df_df)

            # for i in new_df_df:
            #     print(i, type(i["id"], i["id"]))

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


            # dataframe.write \
            #    .format("org.apache.spark.sql.cassandra") \
            #    .mode('append') \
            #    .options(table="tweets", keyspace="tweetrend_test") \
            #    .save()

    sc = SparkContext(appName="Kafka Spark Demo")
    ssc = StreamingContext(sc,5)  #5 = no.of seconds
    ss = SparkSession.builder \
        .appName('SparkCassandraApp') \
        .config('spark.cassandra.connection.host', '10.250.93.207') \
        .config('spark.cassandra.connection.port', '9042') \
        .config('spark.cassandra.output.consistency.level', 'ONE') \
        .getOrCreate()

    message = KafkaUtils.createDirectStream(ssc, topics=["test"],
                kafkaParams={"metadata.broker.list":"localhost:9092"})

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

    message_data.foreachRDD(handle_rdd)
    # message.pprint()

    ssc.start()
    ssc.awaitTermination()