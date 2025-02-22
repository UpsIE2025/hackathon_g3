from kafka import KafkaConsumer
import json

# Configurar el consumidor Kafka
consumer = KafkaConsumer(
    'mensajes_validos',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("📥 Esperando mensajes válidos...")

for message in consumer:
    print(f"✅ Mensaje procesado: {message.value}")
