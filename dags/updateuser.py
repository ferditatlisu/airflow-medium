import sys

dag_path= '/opt/airflow/dags/'
sys.path.insert(1, dag_path)


from datetime import timedelta
from airflow.decorators import dag, task
import pendulum

from commons.mediumredis import MediumRedis
from commons.mediumclient import MediumClient 

@task(task_id='main')
def main():
    redis = MediumRedis()
    users = redis.lrange('users')
    if users:
        client = MediumClient() 
        payload = { "users" : users}
        client.put('http://localhost:8080/users',payload)
    
    return f"{len(users)} users fetched from Redis and updated in internal API"
    
@dag(
    dag_id="update_user",
    schedule_interval=timedelta(minutes=10),
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    max_active_runs=1,
)
def update_user_dag():  
    main()


you_called_dag_here = update_user_dag()
