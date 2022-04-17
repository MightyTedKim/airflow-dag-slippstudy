from datetime import datetime
from airflow.decorators import dag, task
default_args = {
    "owner": "MLOps",
    "description": "An example",
    "start_date": datetime(2022, 1, 1),
}
@dag(
    "example_af_2",
    default_args=default_args,
    catchup=False,
    schedule_interval=None,
    tags=['af_compare'],
)
def example_dag:
    @task()
    def hello_world() -> str:
        return "hello, world!"
		@task()
    def display(msg: str):
        print(msg)
    # XComArgs를 통해 함수 호출 Style로 테스크 제어.
    msg = hello_world()
    display(msg)
example_dag = example_dag()
