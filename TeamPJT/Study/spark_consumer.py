import findspark
findspark.init()

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json


if __name__=="__main__":
    # def utf8_decoder(s):
    #     if s is None:
    #         return None
    #     return s.decode('utf-8')

    sc = SparkContext(appName="Kafka Spark Demo")
    ssc = StreamingContext(sc,15)
    message = KafkaUtils.createDirectStream(ssc, topics=["test"],
                kafkaParams={"metadata.broker.list":"localhost:9092"})

    # words = message.map(lambda x: x[1]).flatMap(lambda x: x.split(" "))
    # wordcount = words.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b)
    # wordcount.pprint()

    # message = message.map(lambda tweet: json.loads(tweet[1]))
    message = message.map(lambda tweet: tweet[1]).flatMap(lambda x:x.split(" "))
    message.pprint()
    # print(eval('"'+message+'"'))
    # message.pprint()

    ssc.start()
    ssc.awaitTermination()