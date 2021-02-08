> cd C:\kafka\kafka_2.13-2.7.0\bin\windows

- zookerper 실행

```
> zookeeper-server-start.bat C:\Kafka\kafka_2.13-2.7.0\config\zookeeper.properties
```

- Kafka 실행

```
> kafka-server-start.bat C:\Kafka\kafka_2.13-2.7.0\config\server.properties
```

- kafka producer 실행

```
> kafka-console-producer.bat --broker-list localhost:9092 --topic test
```

- kafka consumer 실행

```
> kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test
```



- spark consumer 실행

```
> spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.7 spark_consumer.py
```

```
> spark-submit --jars C:\Spark\spark-2.4.7-bin-hadoop2.7\jars\spark-streaming-kafka-0-8-assembly_2.11-2.4.7.jar spark_consumer.py
```

