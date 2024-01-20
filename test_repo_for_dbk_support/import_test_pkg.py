# Databricks notebook source
# MAGIC %sh
# MAGIC pwd
# MAGIC ls -ltr

# COMMAND ----------

# MAGIC %pip install .

# COMMAND ----------

import test_pkg

# COMMAND ----------

test_pkg.test_method()
