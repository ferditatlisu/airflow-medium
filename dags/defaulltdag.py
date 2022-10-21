from datetime import timedelta
from airflow.decorators import dag, task
import pendulum
from airflow.hooks.base_hook import BaseHook

@task(task_id='just_print')
def just_print():
    
    redis_host = BaseHook.get_connection('redis').host

    print('Hello Dev!')
    print(redis_host)
    
@dag(
    dag_id="default_dag",
    schedule_interval=timedelta(minutes=10),
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    max_active_runs=1,
    tags=['default_dag_tag'],
)
def default_dag():  
    just_print()


you_called_dag_here = default_dag()
