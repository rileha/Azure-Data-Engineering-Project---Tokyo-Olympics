# Azure Data Engineering Project Tokyo Olympics

Overview

This project focuses on building an end-to-end data engineering pipeline for data related to the Tokyo Olympic Games, using Data Lake Gen2, Data Factory, Databricks & Synapse Analytics within Azure.

The pipeline ingests data, transforms and analyses displaying the data in a PowerBI report for data-driven insights into the Olympic Games event.

Tech Stack

Azure Data Lake Gen2
Azure Data Factory
Azure Databricks
SQL Database
Power BI

Project Workflow

Data Ingestion

Source: Data from a GitHub repository includes datasets on athletes, coaches, medals, teams, and gender entries.

Pipeline: Using Azure Data Factory (ADF), raw data is extracted and ingested into the Azure Data Lake Storage (ADLS) raw container, establishing a reliable and scalable data storage layer.

Data Preparation and Transformation

Mounting & Loading: Databricks is mounted to the ADLS raw container, enabling seamless access to ingested data.

Cleaning & Structuring: Data types are standardized, and the data is cleaned to create optimized fact and dimension tables, ensuring consistent data quality.

Storage: The transformed data is saved into an ADLS "transformed" container, preparing it for advanced analytics.

Data Warehousing

Transfer: Using ADF, the transformed data is moved from ADLS to a SQL Database within Azure Synapse Analytics.

Storage Optimization: The SQL Database structure allows for efficient query performance, supporting complex analytics and scalable reporting.

Visualization & Reporting

Connecting to Power BI: The SQL Database is connected to Power BI, where views are created, and data is imported to build an interactive dashboard.

Dashboard Insights: The Power BI dashboard delivers key insights, such as athlete and team performance, medal tallies, and demographic breakdowns, empowering stakeholders with data-driven visibility into the Olympic Games.
