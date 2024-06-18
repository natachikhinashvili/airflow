from airflow import DAG
from datetime import datetime, timedelta

default_args= {
    'owner': 'coderj2',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python',
    description='first dag with python',
    start_date=datetime(2021, 10, 6),
    schedule_interval()
)