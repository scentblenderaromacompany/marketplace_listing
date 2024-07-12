from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def dummy_task():
    print("Executing dummy task...")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'marketplace_workflow',
    default_args=default_args,
    description='Marketplace Listing Workflow',
    schedule_interval=timedelta(days=1),
)

task1 = PythonOperator(
    task_id='dummy_task_1',
    python_callable=dummy_task,
    dag=dag,
)

task2 = PythonOperator(
    task_id='dummy_task_2',
    python_callable=dummy_task,
    dag=dag,
)

task1 >> task2
