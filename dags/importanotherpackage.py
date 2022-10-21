import sys

# 
dag_path= '/opt/airflow/dags/'
sys.path.insert(1, dag_path)

from datetime import timedelta
from airflow.decorators import dag, task
import pendulum

from commons.mycommon import print_something_from_another_package

@task(task_id='just_print_something')
def just_print_something():
    something = print_something_from_another_package()
    return something
    
@dag(
    dag_id="import_another_package_dag",
    schedule_interval=timedelta(minutes=10),
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    max_active_runs=1,
    tags=['import_another_package_dag_tag'],
)
def import_another_package_dag():  
    just_print_something()


you_called_dag_here = import_another_package_dag()
