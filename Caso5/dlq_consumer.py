from kafka import KafkaConsumer

# Consumidor de la Dead Letter Queue
dlq_consumer = KafkaConsumer('dead-letter-topic', bootstrap_servers='localhost:9092')

print("📛 Esperando mensajes en la Dead Letter Queue...")

for message in dlq_consumer:
    print(f"⚠️ Mensaje fallido recibido en DLQ: {message.value.decode()}")