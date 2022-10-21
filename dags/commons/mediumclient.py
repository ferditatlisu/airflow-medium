from urllib3.response import HTTPResponse
from urllib3 import PoolManager
import json
import urllib3

class MediumClient():
    pool_manager : PoolManager

    def __init__(self):
        self.pool_manager = urllib3.PoolManager()
        

    def get(self, url):
        res: HTTPResponse = self.pool_manager.request(
            'GET',
            url,
            headers={'Content-Type': 'application/json'})
        
        response_as_dict = json.loads(res.data)
        return response_as_dict
    
    def put(self, url, payload):
        res: HTTPResponse = self.pool_manager.request(
            'PUT',
            url,
            body=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'})
        
        
        response_as_dict = json.loads(res.data)
        return response_as_dict


    def post(self, url, payload):
        res: HTTPResponse = self.pool_manager.request(
            'POST',
            url,
            body=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'})
        
        
        response_as_dict = json.loads(res.data)
        return response_as_dict

