"""
In order to run source queue task we need to open two WSL terminals.
Then we in one we run firstly consumer.py file and in the other one we run consumer.py file.
"""
from pulsar import Client, ConsumerType

SERVICE_URL = "pulsar://localhost:6650"
TOPIC = "my_topic"
SUBSCRIPTION = "sub-1"

client = Client(SERVICE_URL)
consumer = client.subscribe(
    TOPIC,
    SUBSCRIPTION,
    consumer_type=ConsumerType.Shared)