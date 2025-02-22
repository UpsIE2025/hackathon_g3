from kafka import KafkaConsumer
import json

KAFKA_TOPIC = 'publish_subscribe_topic'
KAFKA_SERVER = 'localhost:9092'

def kafka_subscriber_2():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='earliest',
        group_id='shared_subscriber_group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        key_deserializer=lambda k: k.decode('utf-8') if k else None
    )
    for message in consumer:
        if message.key == 'subscriber2':
            print(f"[Subscriber 2] Mensaje recibido: {message.value}")
        else:
            print(f"[Subscriber 2] Mensaje ignorado: {message.value}")

if __name__ == "__main__":
    kafka_subscriber_2()