from kafka import KafkaConsumer
from redis import Redis
import json

KAFKA_TOPIC = 'point_to_point_topic'
KAFKA_SERVER = 'localhost:9092'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

def kafka_consumer_to_redis():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='earliest',
        group_id='group_point_to_point',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    for message in consumer:
        msg = message.value
        redis_client.lpush('mensajes', json.dumps(msg))
        print(f"[Consumer-Kafka] Guardado en Redis: {msg}")

if __name__ == "__main__":
    kafka_consumer_to_redis()