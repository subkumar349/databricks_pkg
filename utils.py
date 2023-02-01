from datetime import datetime


APP_NAME="SPARK UTILS"
CONNECTION="DATABRICKS"

def current_date():
    return datetime.now().isoformat()
