import sys

dag_path= '/opt/airflow/dags/'
sys.path.insert(1, dag_path)

from datetime import datetime, timedelta
from airflow.decorators import dag, task
import pendulum
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from commons.mycommon import print_something_from_another_package

from airflow.models.baseoperator import BaseOperator

class ReadFromFileOperator(BaseOperator):
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        text = None
        with open('random.txt', 'w', encoding='utf-8') as f:
            text = f.read()
            
        return text


#Have to be same otherwise doesnt work as you expect
#schedule_interval=timedelta(minutes=3)


read_from_file_dag = DAG('_read_from_file', schedule_interval=timedelta(minutes=3),start_date=pendulum.datetime(2022, 9, 27, 19, 32, tz="UTC"))

wait_for_write = ExternalTaskSensor(
    task_id='wait_for_write',
    external_dag_id='_write_to_file',
    external_task_id='marker_task',
    execution_delta=timedelta(minutes=2),
    timeout=600,
    allowed_states=['success'],
    failed_states=['failed', 'skipped'],    
    mode="reschedule"
)

    
read_from_write_operator = ReadFromFileOperator(
        task_id="task_read_file", dag=read_from_file_dag, name="{{ task_instance.task_id }}"
    )

wait_for_write >> read_from_write_operator
