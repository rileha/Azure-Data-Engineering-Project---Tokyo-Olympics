# Databricks notebook source
teams = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/teams.csv")
)
teams.show()

# COMMAND ----------

teams.printSchema()

# COMMAND ----------

teams.write \
    .format("csv") \
    .option("header", "true") \
    .mode("overwrite") \
    .save("dbfs:/mnt/tokyoolympic/transformed/dim_teams")

