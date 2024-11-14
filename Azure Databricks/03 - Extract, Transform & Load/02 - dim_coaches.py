# Databricks notebook source
coaches = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/coaches.csv")
)
coaches.show()

# COMMAND ----------

coaches.printSchema()

# COMMAND ----------

coaches.write \
    .format("csv") \
    .option("header", "true") \
    .mode("overwrite") \
    .save("dbfs:/mnt/tokyoolympic/transformed/dim_coaches")

