from datetime import datetime


def check_null(value):
    return value if value is not None else "null"


def transform(tweet):
    res = {
        'timestamp': datetime.utcnow(),
        'created_at': tweet['created_at'],
        'text': tweet['text'],
        'user': {
            'name': tweet['user']['name'],
            'location': check_null(tweet['user']['location']),
            'description': tweet['user']['description'],
            'verified': tweet['user']['verified'],
            'followers_count': tweet['user']['followers_count'],
            'friends_count': tweet['user']['friends_count'],
            'created_at': tweet['user']['created_at']
        },
        'geo': check_null(tweet['geo']),
        'coordinates': check_null(tweet['coordinates']),
        'place': check_null(tweet['place'])
    }
    return res
