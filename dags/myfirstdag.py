import sys

dag_path= '/opt/airflow/dags/'
sys.path.insert(1, dag_path)

from datetime import timedelta
from airflow.decorators import dag, task
import pendulum
from airflow.sensors.external_task import ExternalTaskMarker

from commons.mycommon import print_something_from_another_package

@task(task_id='just_print_hello')
def main():
    print('Hello world')
    name = print_something_from_another_package()
    
    
@dag(
    dag_id="_a_first_dag",
    schedule_interval=timedelta(minutes=10),
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    max_active_runs=1,
    tags=['first_dag'],
)
def dag_main():  
    main()


test = dag_main()
