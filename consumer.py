from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9092")

topic = client.topics['test']

balanced_consumer = topic.get_balanced_consumer(
    consumer_group='testgroup',
    managed=True
)

for message in balanced_consumer:
    if message is not None:
        print message.offset, message.value
