import datetime as dt
import logging
import airflow

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

from common import moduleA as A

with DAG('dag_002',
        start_date=days_ago(2),
        schedule_interval='0 0 * * *',
    ) as dag:

    task_0 = BashOperator(
            task_id='task_0',
            bash_command='echo ${PWD}',
            executor_config={"KubernetesExecutor": {"image": "airflow:55f2cda1"}}
    )

    task_a = PythonOperator(
            task_id='task_a',
            python_callable=A.doSomething,
            executor_config={"KubernetesExecutor": {"image": "airflow:55f2cda1"}}
    )

    task_b = BashOperator(
            task_id='task_b',
            bash_command="./scripts/script_001.sh",
            executor_config={"KubernetesExecutor": {"image": "airflow:55f2cda1"}}
    )

    task_c = BashOperator(
            task_id='task_c',
            bash_command="./scripts/script_002.sh",
            executor_config={"KubernetesExecutor": {"image": "airflow:55f2cda1"}}
    )

    task_d = PythonOperator(
            task_id='task_d',
            python_callable=A.doSomethingElse,
            executor_config={"KubernetesExecutor": {"image": "airflow:55f2cda1"}}
    )

task_0 >> task_a >> [task_b, task_c] >> task_d
