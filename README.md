# Azure Data Engineering Project Tokyo Olympics

https://www.google.com/url?sa=i&url=https%3A%2F%2Flogowik.com%2F2020-logo-vector-1-33028.html&psig=AOvVaw1LbvjGH35zJtpNuuVQwpz9&ust=1731690217076000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJD74fam3IkDFQAAAAAdAAAAABAE![image](https://github.com/user-attachments/assets/209464e5-b7cb-4e55-8900-12f71f680caf)

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

# 2. Data Preparation and Transformation

Mounting & Loading: Databricks is mounted to the ADLS raw container, enabling seamless access to ingested data.

Cleaning & Structuring: Data types are standardized, and the data is cleaned to create optimized fact and dimension tables, ensuring consistent data quality.

Storage: The transformed data is saved into an ADLS "transformed" container, preparing it for advanced analytics.

# 3. Data Warehousing

Transfer: Using Azure Data Factory (ADF), the transformed data is moved from Azure Data Lake Storage (ADLS) to an Azure SQL Database, preparing it for analytics and reporting.

Storage Optimization: The Azure SQL Database is structured to support efficient query performance, making it suitable for complex analytics and scalable reporting.

# 4. Visualization & Reporting

Connecting to Power BI: The SQL Database is connected to Power BI, where views are created, and data is imported to build an interactive dashboard.

Dashboard Insights: The Power BI dashboard delivers key insights, such as athlete and team performance, medal tallies, and demographic breakdowns, empowering stakeholders with data-driven visibility into the Olympic Games.
