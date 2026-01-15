from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

default_args = {
  'owner': 'airflow',
  'depends_on_past': False,
  'start_date': datetime(2026, 1, 11,10),
  'email_on_failure': False
}

def check_updates_api():
    print("Checking for API updates...")

with DAG(
    'data_pipeline',
    default_args=default_args,
    description='Data pipeline for ETL process',
    schedule='@daily',
    tags=["python", "etl", "forecast"]
) as dag:
  check_api = PythonOperator(
    task_id='check_api',
    python_callable=check_updates_api
  )

print(f"DAG object created: {dag}")
print(f"PythonOperator for API check created: {check_api}")