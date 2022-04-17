from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
default_args = {
    'owner': 'airflow',
}
with DAG(
    'example_af_1',
    default_args=default_args,
    description='An example',
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
    tags=['af_compare'],
) as dag:
    def hello_world(**kwargs):
        ti = kwargs['ti']
        ti.xcom_push('msg', 'hello, world!')
    def display(**kwargs):
        ti = kwargs['ti']
        display_msg = ti.xcom_pull(task_ids='hello_world', key='msg')
        print(display_msg)
    hello_world_task = PythonOperator(
        task_id='hello_world',
        python_callable=hello_world,
    )
    display_task = PythonOperator(
        task_id='display',
        python_callable=display,
    )
    hello_world_task >> display_task
