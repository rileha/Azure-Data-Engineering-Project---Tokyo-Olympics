# Databricks notebook source
configs = {
"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "1144d3e4-4890-4afe-b868-a52bf56cf310",
"fs.azure.account.oauth2.client.secret": 'oEv8Q~_Ujtz1DKqLpkHuwzV225UXZdZo2LboSa~x',
"fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/8c3350c5-de17-460b-9cac-d8bf0f1257dd/oauth2/token"
}


dbutils.fs.mount(
source = "abfss://tokyo-olympic-data@tokyoolympicsadls.dfs.core.windows.net",
mount_point = "/mnt/tokyoolympic",
extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls('/mnt/tokyoolympic')
