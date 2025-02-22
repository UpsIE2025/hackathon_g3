from kafka import KafkaConsumer
import redis
import json

# Configurar Kafka Consumer
consumer = KafkaConsumer(
    'channel_adapter',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Configurar Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

print("Esperando mensajes de Kafka...")

for message in consumer:
    data = message.value
    print(f"Mensaje recibido: {data}")
    
    # Almacenar mensaje en Redis con una clave única
    redis_client.set(f"msg:{message.offset}", json.dumps(data))
    print(f"Mensaje almacenado en Redis con clave msg:{message.offset}")
