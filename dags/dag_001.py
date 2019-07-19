import datetime as dt
import logging
import airflow

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from common import moduleA as A

with DAG('dag_001',
        start_date=days_ago(5),
        schedule_interval='0 0 * * *',
    ) as dag:

    task_a = PythonOperator(
            task_id='task_a',
            python_callable=A.doSomething,
            executor_config={"KubernetesExecutor": {"image": "airflow:55f2cda1"}}
    )

task_a
