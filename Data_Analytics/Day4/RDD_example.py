import sys
from pyspark import SparkContext, SparkConf
sc = SparkContext("local", "Pair RDD Example")
marks = [('Rahul', 88), ('Swati', 92), ('Shreya', 83), ('Abhay', 93), ('Rohan', 78)]
output = sc.parallelize(marks).collect()
print(output)