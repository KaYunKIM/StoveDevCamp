import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__ == "__main__":
    sc = SparkContext(appName="Kafka Spark Demo")
    ssc = StreamingContext(sc, 10)  # 10 = no.of seconds
    message = KafkaUtils.createDirectStream(ssc, topics=["test"], 
            kafkaParams={"metadata.broker.list": "localhost:9092"})

    words = message.map(lambda x: x[1]).flatMap(lambda x: x.split(" "))
    wordcount = words.map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)
    wordcount.pprint()

    ssc.start()
    ssc.awaitTermination()