# Databricks notebook source
entriesgender = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/entriesgender.csv")
)
entriesgender.show()

# COMMAND ----------

entriesgender.createOrReplaceTempView("entriesgender")

# COMMAND ----------

gender_by_discipline = spark.sql("""

    SELECT 
        Discipline,
        SUM(Female) as Female,
        SUM(Male) as Male,
        ROUND((SUM(Female) / SUM(Total)), 2) as avg_female,
        ROUND((SUM(Male) / SUM(Total)), 2) as avg_male,
        (SUM(Male) - SUM(Female)) as gender_diff
    FROM entriesgender
    GROUP BY Discipline

""")

gender_by_discipline.show()


# COMMAND ----------

gender_by_discipline.write \
    .format("csv") \
    .option("header", "true") \
    .mode("overwrite") \
    .save("dbfs:/mnt/tokyoolympic/transformed/dim_entriesgender")

