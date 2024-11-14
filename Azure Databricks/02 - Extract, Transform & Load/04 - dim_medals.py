# Databricks notebook source
medals = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/medals.csv")
)
medals.show()

# COMMAND ----------

medals.printSchema()

# Rank, Gold, Silver, Bronze, Total, Rank by Total to Integer

# COMMAND ----------

medals.write \
    .format("csv") \
    .option("header", "true") \
    .mode("overwrite") \
    .save("dbfs:/mnt/tokyoolympic/transformed/dim_medals")

