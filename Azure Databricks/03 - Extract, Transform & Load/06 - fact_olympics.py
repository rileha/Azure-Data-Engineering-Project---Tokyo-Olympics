# Databricks notebook source
athletes = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/athletes.csv")
)
entriesgender = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/entriesgender.csv")
)
medals = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/medals.csv")
)
teams = (
    spark.read.format("csv")
    .option("header", "true")
    .option("InferSchema", "true")
    .load("/mnt/tokyoolympic/raw/teams.csv")
)

# COMMAND ----------

athletes.createOrReplaceTempView("athletes")
teams.createOrReplaceTempView("teams")
medals.createOrReplaceTempView("medals")
entriesgender.createOrReplaceTempView("gender")


# COMMAND ----------

athletes_teams_medals_gender = spark.sql("""
                                   
SELECT
    a.PersonName as athlete_name,
    t.Country as country,
    t.Discipline as discipline,
    t.Event as event,
    g.Male as men_in_discipline,
    g.Female as women_in_discipline,
    g.Total as total_in_discipline,
    m.Gold as nation_total_gold,
    m.Silver as nation_total_silver,
    m.Bronze as nation_total_bronze,
    m.Total as nation_medal_total
FROM teams as t
JOIN gender as g
    ON t.Discipline = g.Discipline
JOIN medals as m
    ON t.Country = m.TeamCountry 
JOIN athletes as a
    ON t.Country = a.Country AND t.Discipline = a.Discipline
ORDER BY country
"""
)

athletes_teams_medals_gender.show()

# COMMAND ----------

athletes_teams_medals_gender.write \
    .format("csv") \
    .option("header", "true") \
    .mode("overwrite") \
    .save("dbfs:/mnt/tokyoolympic/transformed/fact_olympics")

