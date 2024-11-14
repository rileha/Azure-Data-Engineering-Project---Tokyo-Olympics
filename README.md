# Azure Data Engineering Project Tokyo Olympics

![Tokyo Logo](https://github.com/user-attachments/assets/ab55867b-ec28-416c-9d0d-9f147286f542)


# Overview

This project focuses on building an end-to-end data engineering pipeline for data related to the Tokyo Olympic Games, using Data Lake Gen2, Data Factory, Databricks & Synapse Analytics within Azure.

The pipeline ingests data, transforms and analyses displaying the data in a PowerBI report for data-driven insights into the Olympic Games event.

# Tech Stack

Azure Data Lake Gen2
Azure Data Factory
Azure Databricks
SQL Database
Power BI

# Project Workflow

# 1. Data Ingestion

Source: Data from a GitHub repository includes datasets on athletes, coaches, medals, teams, and gender entries.

Pipeline: Using Azure Data Factory (ADF), raw data is extracted and ingested into the Azure Data Lake Storage (ADLS) raw container, establishing a reliable and scalable data storage layer.

<img width="1211" alt="1  Raw Ingestion from GitHub - ADF" src="https://github.com/user-attachments/assets/b2a4198b-479c-469f-9f5a-16fd735c4795">

# 2. Data Preparation and Transformation

Mounting & Loading: Databricks is mounted to the ADLS raw container, enabling seamless access to ingested data.

Cleaning & Structuring: Data types are standardized, and the data is cleaned to create optimized fact and dimension tables, ensuring consistent data quality.

Storage: The transformed data is saved into an ADLS "transformed" container, preparing it for advanced analytics.

<img width="1438" alt="2  fact_olympic JOIN Databricks" src="https://github.com/user-attachments/assets/5fe66e55-9498-46d2-a0a3-fd502d883f73">

# 3. Data Warehousing

Transfer: Using Azure Data Factory (ADF), the transformed data is moved from Azure Data Lake Storage (ADLS) to an Azure SQL Database, preparing it for analytics and reporting.

Storage Optimization: The Azure SQL Database is structured to support efficient query performance, making it suitable for complex analytics and scalable reporting.

<img width="1438" alt="3  transformed to SQL DB ADF" src="https://github.com/user-attachments/assets/5abe1b98-2fa1-4150-b681-a19d10d18531">

# 4. Visualization & Reporting

Connecting to Power BI: The SQL Database is connected to Power BI, where views are created, and data is imported to build an interactive dashboard.

<img width="1557" alt="4  Power BI Dashboard" src="https://github.com/user-attachments/assets/7ec4742b-33b7-469c-a013-e57847bec577">


Dashboard Insights: The Power BI dashboard delivers key insights, such as athlete and team performance, medal tallies, and demographic breakdowns, empowering stakeholders with data-driven visibility into the Olympic Games.
