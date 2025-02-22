consumer = KafkaConsumer(
    'dead_letter_channel',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Esperando mensajes fallidos en Dead Letter Channel...")

for message in consumer:
    print(f"Mensaje fallido recibido: {message.value}")
