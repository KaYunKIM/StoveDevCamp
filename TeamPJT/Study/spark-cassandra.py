import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=localhost pyspark-shell'

from pyspark import SparkContext
from pyspark.sql import SQLContext, SparkSession

spark = SparkSession.builder \
     .appName('SparkCassandraApp') \
     .config('spark.cassandra.connection.host', 'localhost') \
     .config('spark.cassandra.connection.port', '9042') \
     .config('spark.cassandra.output.consistency.level','ONE') \
     .master('local[2]') \
     .getOrCreate()


# sc = SparkContext("local", "lab")  # keyspace name=lab
# sqlContext = SQLContext(sc)

sqlContext = SQLContext(spark)
ds = sqlContext \
     .read\
     .format('org.apache.spark.sql.cassandra') \
     .options(table='movies', keyspace='lab') \
     .load() \
     # .save()

ds.show(10)