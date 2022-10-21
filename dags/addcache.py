import sys

dag_path= '/opt/airflow/dags/'
sys.path.insert(1, dag_path)


from datetime import timedelta
from airflow.decorators import dag, task
import pendulum
from airflow.hooks.base_hook import BaseHook

from operators.slackoperator import SlackOperator 
from commons.mediumelastic import MediumElastic
from commons.mediumredis import MediumRedis

def get_elastic_query():
    return {
            "query": {
                "match_all": {}
            }
    }

@task(task_id='main')
def main():
    elastic = MediumElastic()
    elastic_data = elastic.search(get_elastic_query())
    if elastic_data and len(elastic_data) > 0:
        redis = MediumRedis()
        for data in elastic_data:
            redis.set(data["id"], data)
    
    return f"{len(elastic_data)} items fetched from Elastic and updated in Redis"


def on_failure_callback(context):    
    slack = SlackOperator(dag_name='add_cache')
    slack.execute(context)
    
@dag(
    dag_id="add_cache",
    schedule_interval=timedelta(minutes=10),
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    max_active_runs=1,
    default_args={
        'on_failure_callback': on_failure_callback,
    }
)
def add_cache_dag():  
    main()



you_called_dag_here = add_cache_dag()
