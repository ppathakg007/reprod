# Databricks notebook source
# MAGIC %sh
# MAGIC python setup.py build_ext --inplace --build-lib=/tmp/

# COMMAND ----------

# MAGIC %sh
# MAGIC mkdir /tmp/package
# MAGIC cp -r * /tmp/package
# MAGIC cd /tmp/package/
# MAGIC pip install ./

# COMMAND ----------

# MAGIC %sh
# MAGIC #cd /Workspace/Repos/.internal/5a4de209db_commits/35963722b91e1c315f7799deb68067f42e547009/test_repo_for_dbk_support
# MAGIC mkdir  /Workspace/Repos/test

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install --upgrade pip

# COMMAND ----------


