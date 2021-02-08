from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark import SparkConf

logFile = "README.md" 
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

# spark.stop()

sc = SparkContext.getOrCreate(SparkConf())
lines = sc.textFile("README.md")
print(lines)