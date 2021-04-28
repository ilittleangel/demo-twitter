import json
import tweepy
from utils import elastic
from utils import tweets
from utils import kafka
from settings import credentials, twitter_filters, topic


class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        doc = tweets.transform(tweet)
        print(f"{tweet['user']['name']} --> {tweet['text']}")
        elastic.index(es, doc)
        kafka.producer.produce(topic,
                               key=f"{tweet['user']['name']}-{doc['timestamp']}",
                               value=data,
                               callback=kafka.acked)

    def on_error(self, status):
        print(status)
        return False


if __name__ == '__main__':
    try:
        es = elastic.create_connection()
        auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
        auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
        stream = tweepy.Stream(auth=auth, listener=MyStreamListener())
        stream.filter(track=twitter_filters)

    except KeyboardInterrupt as k:
        print('Bye!')
