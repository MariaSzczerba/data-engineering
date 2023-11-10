import csv
from pulsar import Client, ConsumerType

SERVICE_URL = "pulsar://localhost:6650"
TOPIC = "my_topic"

client = Client(SERVICE_URL)
producer = client.create_producer(
    TOPIC
)

with open('user_records_large.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

# Select 1000 rows
selected_rows = rows[:1000]

for row in selected_rows:
    producer.send(row)
