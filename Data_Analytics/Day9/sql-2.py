from pyspark.sql import SparkSession
spark = (SparkSession.builder.appName("SparkSQL Demo").getOrCreate())
csv_file = "appl_stock.csv"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("stock_table")
spark.sql("""SELECT Date, Open, Close FROM stock_table WHERE Close < 500""").show()
df.filter((df['Close'] < 500) & (df ['Open'] > 200)).select (['Open', 'Close']).show(10000)