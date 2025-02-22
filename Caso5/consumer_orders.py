from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'orders_channel',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Esperando mensajes de órdenes...")

for message in consumer:
    print(f"Orden recibida: {message.value}")
