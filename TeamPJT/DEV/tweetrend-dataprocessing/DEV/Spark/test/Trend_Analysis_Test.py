import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import *
import json

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=10.250.93.207:9042 pyspark-shell'

def tweet_data(table, keyspace):
    global sqlContext

    dataframe = sqlContext.read \
        .format("org.apache.spark.sql.cassandra") \
        .options(table=table, keyspace=keyspace) \
        .load() \
        .filter((col("topic")=="covid-19") & (col("datehour")==-1311406)) \
        .select("topic", "message", "author_id", "place_id", "source", "referenced_tweets", "includes")    
    
    return dataframe

sc = SparkContext(appName="Kafka Spark Demo")
sqlContext = SQLContext(sc)
ss = SparkSession.builder \
    .appName('SparkCassandraApp') \
    .config('spark.cassandra.connection.host', '10.250.93.207') \
    .config('spark.cassandra.connection.port', '9042') \
    .config('spark.cassandra.output.consistency.level', 'ONE') \
    .getOrCreate()

## return tweets dataframe
tweets = tweet_data("tweets", "tweetrend")
tweets.show()
print()

## summary statistics
#tweets.describe().show()
#print()

## count total
tweets_total = tweets.count()
print('total_count: ', tweets_total)

## count user_id
tweets_author = tweets.select("author_id").distinct().count()
print('user_count: ', tweets_author)

## count region
place_id = tweets.groupBy("place_id").count()
place_id.show()

place_info = tweets.select("place_id", "includes") \
        .withColumn("places", col("includes").getItem("places")[0]) \
        .withColumn("id", col("places").getItem("id")) \
        .withColumn("country_code", col("places").getItem("country_code")) \
        .na.drop() \
        #.show()

place = place_info.select("place_id", "id", "country_code") \
        .where(place_info.place_id == place_info.id) \
        
place.show()

print('tweets_place:', tweets.select("place_id").na.drop().count())
print('compare_places:', place.count())
             
tweets_place = place.groupBy("country_code").count()
tweets_place.show()
            

## count source
tweets_source = tweets.groupBy("source").count()
#tweets_source.show()


## count retweet
tweets_retweet = tweets.select("referenced_tweets")
retweet = tweets_retweet \
          .withColumn("retweet_type", col("referenced_tweets").getItem("type")[0]) \
          .withColumn("retweet_id", col("referenced_tweets").getItem("id")[0]) \
          #.show()

retweet_count = retweet.groupBy("retweet_type").count()
#retweet_count.show()

# words = message.map(lambda x: json.loads(x[1])).flatMap(lambda x: x.split(" "))
# wordcount = words.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b)
# wordcount.pprint()
