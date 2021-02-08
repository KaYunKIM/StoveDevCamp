from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import findspark
import json


if __name__ == "__main__":
    findspark.init()

    # SparkContext represents the connection to a Spark cluster
    # Only one SparkContext may be active per JVM
    sc = SparkContext(appName="Kafka Spark Demo")

    # Creating a streaming context with batch interval of 10 sec
    # As the main point of entry for streaming, StreamingContext handles the streaming application's actions,
    # including checkpointing and transformations of the RDD.
    ssc = StreamingContext(sc, 10)

    # DStream(RDD 로 이루어진 객체) 반환
    kafkaStream = KafkaUtils.createDirectStream(
        ssc, topics=["test"], kafkaParams={"metadata.broker.list": "localhost:9092"}
    )

    # Parse Twitter Data as json
    json_stream = kafkaStream.map(lambda tweet: json.loads(tweet[1]))
    json_stream.pprint()
    # parsed = json_stream.map(lambda tweet: tweet_filter(tweet))
    # parsed.foreachRDD(lambda x: x.saveToCassandra("bts", "tweet_dataset"))
    # parsed.pprint()

    # Count Twitter Data by word
    # words = kafkaStream.map(lambda x: x[1]).flatMap(lambda x: x.split(" "))
    # wordcount = words.map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)
    # wordcount.pprint()

    # Start Execution of Streams
    ssc.start()
    ssc.awaitTermination()