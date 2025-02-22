from kafka import KafkaConsumer
import json
import redis

# Conectar a Redis
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Configurar el consumidor Kafka
consumer = KafkaConsumer(
    'mensajes_invalidos',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("📥 Esperando mensajes inválidos...")

for message in consumer:
    print(f"❌ Mensaje inválido recibido: {message.value}")
    redis_client.lpush("mensajes_invalidos", json.dumps(message.value))
    print("⚠️ Mensaje almacenado en Redis")
