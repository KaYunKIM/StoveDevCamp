import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

from datetime import datetime
import json

#Cassandra
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=10.250.93.207:9042 pyspark-shell'


if __name__=="__main__":
    def handle_rdd(rdd):
        if not rdd.isEmpty():
            global ss, schema_list
            dataframe = ss.createDataFrame(rdd, schema = schema_list)
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

    if message.map(lambda tweet: tweet['includes']):
        if message.map(lambda tweet: tweet['includes']['tweets']):
            tweets_data = message.map(lambda tweet: tweet['includes']['tweets'])

            for data in tweets_data:
                if data["in_reply_to_user_id"]:
                    data["in_reply_to_user_id"] = int(data["in_reply_to_user_id"])
                
                if data["referenced_tweets"]:
                    data["referenced_tweets"]["id"] = int(data["referenced_tweets"]["id"])

                data["id"] = int(data["id"])
                data["author_id"] = int(data["author_id"])
        
        if message.map(lambda tweet: tweet['includes']['users']):
            users_data = message.map(lambda tweet: tweet['includes']['users'])

            for data in users_data:
                data["id"] = int(data["id"])
        
        # message = message.map(lambda tweet: tweet['includes'])
    
    message = message.map(lambda tweet: tweet['data'](
        tweet['data']['id'] = int(tweet['data']['id']),
        tweet['data']['author_id'] = int(tweet['data']['author_id']),

        if tweet['data']['conversation_id']:
            tweet['data']['conversation_id'] = int(tweet['data']['conversation_id']),
        
        if tweet['data']['in_reply_to_user_id']:
            tweet['data']['in_reply_to_user_id'] = int(tweet['data']['in_reply_to_user_id']),
        )
    )
        

    # message = message.map(lambda tweet: (
    #     tweet['data']
    #     tweet['includes'],
    #     )
    # )

    # cassandra_reshape
    def reform_message(message, urls):
    '''
    :param message: str, tweet->text
    :param urls: str, entities->urls
    :return: str, new message with expanded url
    '''
    for url in urls:
        new_msg = message[:url['start'] - 1] + url['expanded_url'] if url['start'] > 0 else url['expanded_url']
        new_msg = new_msg + message[url['end']:] if url['end'] < len(message) else new_msg

    return new_msg


    def reshape(json_file, topic):
        '''
        :param json_file: dict/json, a set of data and includes
        :param topic: str, topic of the json_file
        :return: dict/json, reshaped data for insert into tweets
        '''
        row = json_file['data'].copy()

        if 'includes' in json_file:
            row['includes'] = json_file['includes']

            if 'tweets' in row['includes']:
                for tweet in row['includes']['tweets']:
                    tweet['text'] = reform_message(tweet['text'], tweet['entities']['urls']) if 'entities' in tweet else tweet['text']

            if 'media' in row['includes']:
                for medium in row['includes']['media']:
                    if 'public_metrics' in medium:
                        medium['view_count'] = medium['public_metrics']['view_count']

                        del medium['public_metrics']

        row['topic'] = topic

        if 'referenced_tweets' in row and row['referenced_tweets'][0]['type']=='retweeted':
            row['text'] = row['includes']['tweets'][0]['text']

        elif 'entities' in row and 'urls' in row['entities']:
            row['text'] = reform_message(row['text'], row['entities']['urls'])

        if 'geo' in row:
            row['place_id'] = row['geo']['place_id']

            del row['geo']

        created_at = row['created_at'].split('T')
        row['datehour'] = -int(''.join(created_at[0].split('-')[1:]) + ''.join(created_at[1].split(':')[:2]))

        row['stored_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return json.loads(json.dumps(row).replace('\'text\':', '\'message\':'))

    message = reshape(tweet, 'covid-19')
    schema_list = list(message.keys())

    message.foreachRDD(handle_rdd)
    # message.pprint()

    ssc.start()
    ssc.awaitTermination()