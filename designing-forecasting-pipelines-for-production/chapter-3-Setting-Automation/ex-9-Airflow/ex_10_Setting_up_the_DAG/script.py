# Import required classes
#Import the DAG and PythonOperator classes from Airflow.
#Set the start date as 7th July, 2025.
#Set email_on_failure to False.

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

default_args = {
  'owner': 'airflow',
  # Define the arguments
  'depends_on_past': False,
  'start_date': datetime(2026, 1, 11,10),
  'email_on_failure': False}

print(f"DAG configured to start on {default_args['start_date']}")
