# from pyspark.sql import SparkSession as ss

# spark = ss.builder.appName("test").getOrCreate()

# dept = [("Finance", 10), ("Marketing", 20), ("Sales", 30)]
# deptCol = ["name", "id"]

# rdd = spark.sparkContext.parallelize(dept)
# df = rdd.toDF()

#df = spark.createDataFrame(data=dept, schema=["id"])
# df.show()


import TwitterAPI as t
print(t.__file__)