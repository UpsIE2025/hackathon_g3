from kafka import KafkaProducer
import json

# Configurar el productor Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def publish_message(topic, message):
    producer.send(topic, message)
    producer.flush()
    print(f"📤 Mensaje enviado a {topic}: {message}")

# Simulación de mensajes válidos e inválidos
messages = [
    {"id": 1, "texto": "Mensaje válido"},
    {"id": 2, "texto": ""},  # ❌ Inválido: Texto vacío
    {"texto": "Sin ID"},  # ❌ Inválido: Falta el ID
]

for msg in messages:
    if "id" in msg and msg["texto"]:
        publish_message("mensajes_validos", msg)
    else:
        publish_message("mensajes_invalidos", msg)
