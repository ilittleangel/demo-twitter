from elasticsearch import Elasticsearch
from settings import es_index, es_nodes


def create_connection():
    try:
        es = Elasticsearch(es_nodes)
        return es
    except Exception as e:
        print(f"Unable to connect Elasticsearch: {e}")


def index(es, doc):
    try:
        res = es.index(index=es_index, body=doc)
        if res['result'] != "created":
            print(f"Index was unexpected: {res['result']}")
    except Exception as e:
        print(f"Failure to index: {e}")
