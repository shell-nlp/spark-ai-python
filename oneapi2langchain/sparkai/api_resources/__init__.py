import os

# Path of a file with an API key, whose contents can change. Supercedes
# `api_key` if set.  The main use case is volume-mounted Kubernetes secrets,
# which are updated automatically.

print("getting config from env: SPARK_API_BASE,SPARK_APP_ID,SPARK_API_KEY,SPARK_API_SECRET")
api_base = os.environ.get("SPARK_API_BASE", "wss://spark-api.xf-yun.com/v2.1/chat")
api_type = os.environ.get("SPARK_API_TYPE", "spark")
api_domain = os.environ.get("SPARK_DOMAIN", "plugin")

app_id = os.environ.get("SPARK_APP_ID")
api_key = os.environ.get("SPARK_API_KEY")
api_secret = os.environ.get("SPARK_API_SECRET")
