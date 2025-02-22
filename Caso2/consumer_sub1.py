from kafka import KafkaConsumer
import json

KAFKA_TOPIC = 'publish_subscribe_topic'
KAFKA_SERVER = 'localhost:9092'

def kafka_subscriber_1():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='earliest',
        group_id='shared_subscriber_group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        key_deserializer=lambda k: k.decode('utf-8') if k else None
    )
    for message in consumer:
        if message.key == 'subscriber1':
            print(f"[Subscriber 1] Mensaje recibido: {message.value}")
        else:
            print(f"[Subscriber 1] Mensaje ignorado: {message.value}")

if __name__ == "__main__":
    kafka_subscriber_1()