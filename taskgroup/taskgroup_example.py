from datetime import datetime
from typing import List
from airflow.operators.dummy import DummyOperator
from airflow.utils.task_group import TaskGroup
from airflow.decorators import dag
@dag(
    "taskgroup_example",
    default_args=default_args,
    catchup=False,
    schedule_interval=None,
    tags=['taskgroup']
)
def example_dag() -> None:
    ops: List[DummyOperator] = []
    with TaskGroup(group_id="task_group"):
        for i in range(5):
            op = DummyOperator(task_id=f"task_{i}")
            ops.append(op)
            if i > 0:
                ops[i - 1] >> op
example_dag = example_dag()
