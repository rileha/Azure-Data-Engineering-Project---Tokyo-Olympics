# Databricks notebook source
athletes = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/athletes.csv")
)
athletes.show()

# COMMAND ----------

athletes.printSchema()

# COMMAND ----------

athletes.write \
    .format("csv") \
    .option("header", "true") \
    .mode("overwrite") \
    .save("dbfs:/mnt/tokyoolympic/transformed/dim_athletes")

