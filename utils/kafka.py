from confluent_kafka import Producer
import socket
from settings import brokers

conf = {'bootstrap.servers': brokers, 'client.id': socket.gethostname()}
producer = Producer(conf)


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))
