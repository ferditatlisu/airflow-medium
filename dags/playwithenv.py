from datetime import timedelta
from airflow.decorators import dag, task
import pendulum
from airflow.models import Variable


@task()
def play_with_env():
    print('Hello Dev!')
    
    Variable.set('key', 'my_value')
    variable = Variable.get('key', 'default_value')
    print(f"It must be 'my_value' from key : {variable}")
    
    
@dag(
    dag_id="play_with_env_dag",
    schedule_interval=timedelta(minutes=10),
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
)
def play_with_env_dag():  
    play_with_env()


you_called_dag_here = play_with_env_dag()
