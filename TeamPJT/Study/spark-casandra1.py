import os
os.environ['PYSPARK_SUBMIT_ARGS'] = \
    '--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.1' \
    ' --conf spark.cassandra.connection.host=localhost pyspark-shell'

# spark.sql.extensions = com.datastax.spark.connector.CassandraSparkExtensions

from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "lab")  # keyspace name=lab
sqlContext = SQLContext(sc)  # SQL 작업을 하기 위한 SQL Context 생성

## 주어진 keyspace와 table에 맞춰 dataframe 반환
def load_and_get_table_DF(keyspace_name, table_name):
    table_DF = sqlContext\.read\
        .format("org.apache.spark.sql.cassandra")\
        .options(table=table_name, keyspace=keyspace_name)\
        .load()
    return table_DF

## movies, ratings dataframe load
movies = load_and_get_table_DF("lab","movies")
ratings = load_and_get_table_DF("lab","ratings")

movies.show(10)
