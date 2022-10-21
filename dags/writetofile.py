from datetime import timedelta
import pendulum
from airflow import DAG
from airflow.decorators import task
from airflow.sensors.external_task import ExternalTaskMarker
from airflow.models.baseoperator import BaseOperator


class WriteToFileOperator(BaseOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        with open('random.txt', 'w', encoding='utf-8') as f:
            f.write("Write something to file")
            
        return None


write_to_file_dag = DAG('_write_to_file', schedule_interval=timedelta(minutes=3), start_date=pendulum.datetime(2022, 9, 27, 19, 30, tz="UTC"))

marker_task = ExternalTaskMarker(task_id="marker_task", 
                        external_dag_id="_read_from_file",
                        external_task_id="task_read_file")

write_to_file_operator = WriteToFileOperator(
        task_id="task_write_file", dag=write_to_file_dag
    )

write_to_file_operator >> marker_task
