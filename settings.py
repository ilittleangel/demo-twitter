import os

es_nodes = ['http://localhost:9200']
es_index = 'tweets'

credentials = {
    'consumer_key': os.environ.get('CONSUMER_KEY'),
    'consumer_secret': os.environ.get('CONSUMER_SECRET'),
    'access_token': os.environ.get('ACCESS_TOKEN'),
    'access_token_secret': os.environ.get('ACCESS_TOKEN_SECRET')
}
