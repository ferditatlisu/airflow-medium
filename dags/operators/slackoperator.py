from airflow.models.baseoperator import BaseOperator
from commons.mediumclient import MediumClient

class SlackOperator(BaseOperator):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        print('send slack message with webhook!')
        task_instance = context['task_instance']
        slack_msg = f"""
            :red_circle: Task Failed. 
            Task: {task_instance.task_id}  
            Dag: {task_instance.dag_id} 
            Execution Time: {context.get('execution_date')}  
            Log Url: {task_instance.log_url} 
            """
        
        request_body = {"text": f"{slack_msg}"}
        client = MediumClient()
        client.post(request_body)
        
        return None