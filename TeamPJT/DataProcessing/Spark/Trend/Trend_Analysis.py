import senti_word

import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import *

from mongoengine import *

from collections import Counter
from konlpy.tag import Okt
import json, time, datetime, copy

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=10.250.93.207:9042 pyspark-shell'

def tweet_data(table, keyspace, datehour):
    global sqlContext, DB_topic

    dataframe = sqlContext.read \
        .format("org.apache.spark.sql.cassandra") \
        .options(table=table, keyspace=keyspace) \
        .load() \
        .filter((col("topic")==DB_topic) & (col("datehour")==datehour)) \
        .select("topic", "message", "author_id", "place_id", "source", "referenced_tweets", "includes", "lang")    
    
    return dataframe

sc = SparkContext(appName="Trend Analysis")
sqlContext = SQLContext(sc)
ss = SparkSession.builder \
    .appName('SparkCassandraApp') \
    .config('spark.cassandra.connection.host', '10.250.93.207') \
    .config('spark.cassandra.connection.port', '9042') \
    .config('spark.cassandra.output.consistency.level', 'ONE') \
    .getOrCreate()

DB_topic = "covid-19"

#Real Time
while True:
    now = datetime.datetime.now()
    search = str(now - datetime.timedelta(hours=9, minutes=1))
    datehour = search[6:7]+search[8:10]+search[11:13]+search[14:16]
    try:
        ## return tweets dataframe
        tweets = tweet_data("tweets", "tweettrend", datehour)
    except:
        pass
    

    ## kor tweets only
    tweets = tweets.filter(tweets.lang == "ko")
    

    ## summary statistics
    #tweets.describe().show()


    ## total count
    total = tweets.count()
    if total == 0:
        continue


    ## user_id count
    author = tweets.select("author_id").distinct().count()


    ## region count
    place_id = tweets.groupBy("place_id").count()

    place_info = tweets.select("place_id", "includes") \
            .withColumn("places", col("includes").getItem("places")[0]) \
            .withColumn("id", col("places").getItem("id")) \
            .withColumn("country_code", col("places").getItem("country_code")) \
            .na.drop() \
            #.show()

    place = place_info.select("place_id", "id", "country_code") \
            .where(place_info.place_id == place_info.id) \
            
    #place.show()
    #print('tweets_place:', tweets.select("place_id").na.drop().count())
    #print('compare_places:', place.count())
                
    tweets_place = place.groupBy("country_code").count()
    tweets_place = tweets_place.toJSON().map(lambda j: json.loads(j)).collect()

    region = {}
    for i in tweets_place:
        region[i['country_code']] = i['count']


    ## source count
    tweets_source = tweets.groupBy("source").count()
    tweets_source = tweets_source.na.drop().toJSON().map(lambda j: json.loads(j)).collect()

    source = {}
    for i in tweets_source:
        if '.' in i['source']:
            i['source'] = ''.join(i['source'].split('.'))
        if i['source'][0] == '$':
            i['source'] = i['source'][1:]
        source[i['source']] = i['count']


    ## retweet count
    tweets_referenced_tweets = tweets.select("referenced_tweets")
    tweets_retweet = tweets_referenced_tweets \
            .withColumn("retweet_type", col("referenced_tweets").getItem("type")[0]) \
            .withColumn("retweet_id", col("referenced_tweets").getItem("id")[0]) \
            #.show()

    retweet_count = tweets_retweet.groupBy("retweet_type").count()
    retweet_count = retweet_count.na.drop().toJSON().map(lambda j: json.loads(j)).collect()
    retweet =0

    for i in retweet_count:
        if i['retweet_type'] == 'retweeted':
            retweet = i['count']
            break

    
    ## related words count 
    okt = Okt()
    tweet_message = tweets.select("message").collect()

    keywords = []

    for i in tweet_message:
        tweet_word = okt.nouns(i['message'])
        keywords.extend(tweet_word)

    word_count = dict(Counter(keywords).most_common(int(len(keywords)*0.05)))
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(word_count)-1, -1, -1):
        if word_count[i][1] == 1 or word_count[i][1] == 2:
            word_count.pop()
        else:
            break
    
    stop_file_name = open('Stopwords.txt', 'r', encoding='utf-8')
    stop_words = list(stop_file_name.readlines())

    new_word_list = copy.deepcopy(word_count)

    for i in new_word_list:
        if i[0] + '\n' in stop_words:
            word_count.remove((i[0], i[1]))

    related_words = {}
    reputation = {
            'positive': 0,
            'negative': 0,
            'neutral': 0
            }

    for j in word_count:
        word_analysis = senti_word.text_analysis(j[0])
        if word_analysis[0] == '진자':
            related_words['확진자'] = (j[1], word_analysis[1])
        elif word_analysis[0] == '거리':
            related_words['거리두기'] = (j[1], word_analysis[1])
        else:    
            related_words[word_analysis[0]] = (j[1], word_analysis[1])
        if word_analysis[1] > 0:
            reputation['positive'] += 1
        elif word_analysis[1] < 0:
            reputation['negative'] += 1
        else:
            reputation['neutral'] += 1


    ## topic
    topic = DB_topic


    ## timestamp 
    collected_at = datetime.datetime(2021,int(datehour[:-6]),int(datehour[-6:-4]),int(datehour[-4:-2]),int(datehour[-2:])).timestamp()
    collected_at = int(collected_at+32400)


    ## Mongo DB insert
    connect('trend', username='bigsmile', password='bigsmile123', authentication_source='admin', host='10.250.93.97',
        port=27017)

    class Region(DynamicEmbeddedDocument):
        pass

    class Keyword(DynamicEmbeddedDocument):
        pass

    class Reputation(EmbeddedDocument):
        positive = IntField()
        negative = IntField()
        neutral = IntField()

    class Source(DynamicEmbeddedDocument):
        pass

    class TimeTrendKor(Document):
        topic = StringField(required=True)
        collected_at = IntField(required=True, unique=True)
        total_counts = IntField(required=True)
        user_counts = IntField(required=True)
        retweet_counts = IntField(required=True)
        region = EmbeddedDocumentField(Region)
        related_words = EmbeddedDocumentField(Keyword)
        reputation = EmbeddedDocumentField(Reputation)
        source = EmbeddedDocumentField(Source)
        
    ## insert form
    try:
        insert = TimeTrendKor(
        topic=topic, 
        collected_at=collected_at, 
        total_counts = total, 
        user_counts = author, 
        retweet_counts = retweet, 
        region = region, 
        related_words = related_words, 
        reputation = reputation, 
        source = source)
        insert.save()

        print('MongoDB Schema')
        print('topic: ', topic)
        print('collected_at: ', collected_at)
        print('total_count: ', total)
        print('user_count: ', author)
        print('retweet_count: ', retweet)
        print('region_count: ', region)
        print('related_words: ', related_words)
        print('reputation: ', reputation)
        print('source: ', source)
        
        ## get tweets from Cassandra DB every 1 minute
        time.sleep(50)
    except:
        pass
    