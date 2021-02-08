import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.sql import SparkSession, SQLContext
import json

#Cassandra
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=10.250.93.207:9042 pyspark-shell'

def tweet_data(table, keyspace):
    global sqlContext
    dataframe = sqlContext.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table=table, keyspace=keyspace)\
        .load()

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


rdd = tweets.rdd.flatmap(lambda x: list(x))
rdd.pprint()

## dataframe to JSON
# tweets = tweets.toJSON().map(lambda x: json.loads(x)).take(1)
# print(type(tweets), tweets)




# words = message.map(lambda x: json.loads(x[1])).flatMap(lambda x: x.split(" "))
# wordcount = words.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b)
# wordcount.pprint()

# transform.foreachRDD(handle_rdd)


## show all entries in 'data', 'includes' colums
dataframe.select('data', 'includes').show(10)

