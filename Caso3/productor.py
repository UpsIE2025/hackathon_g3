from kafka import KafkaProducer
import json
import redis

# Configuración de Kafka
KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'Datatype'

# Configuración de Redis
REDIS_SERVER = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# Conexión a Kafka (Productor)
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Conexión a Redis
r = redis.Redis(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)

def send_to_kafka(data):
    """Envia el mensaje a Kafka"""
    producer.send(TOPIC_NAME, data)
    producer.flush()

def store_in_redis(data):
    """Almacena el mensaje en Redis"""
    r.set(data['id_cliente'], json.dumps(data))
