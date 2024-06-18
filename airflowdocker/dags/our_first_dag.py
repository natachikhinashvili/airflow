from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag',
    default_args=default_args,
    description='first airflow dag',
    start_date=datetime(2024, 7, 18, 2),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command = "echo hello world"
    )

    task2 = BashOperator(
        task_id='second_task'
        bash_command='im executed after task1'
    )

    task1.set_downstream(task2)