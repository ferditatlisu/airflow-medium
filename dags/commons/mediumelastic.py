
from typing import Dict
from uuid import uuid4
from elasticsearch.client import Elasticsearch
import json


class MediumElastic:
    es : Elasticsearch
    
    def __init__(self):
        self.es = Elasticsearch("localhost:9200")
        
    def search(self, query : Dict):
        res = self.es.search(index="index", from_=0, size=1, body=query)

        hits = json.loads(json.dumps(res))["hits"]["hits"]
        if len(hits) != 0:
            documents = []
            for hit in hits:
                document = json.loads(json.dumps(hit))["_source"]
                documents.append(document)
                
            return document