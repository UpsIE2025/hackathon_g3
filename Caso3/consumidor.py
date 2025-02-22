from kafka import KafkaConsumer
import json

# Configuración de Kafka
KAFKA_SERVER = 'localhost:9092'
TOPIC_NAME = 'Datatype'

# Conexión a Kafka (Consumidor)
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_SERVER,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_from_kafka():
    """Consume el primer mensaje de Kafka"""
    for message in consumer:
        # Cerrar el consumidor después de recibir el primer mensaje
        consumer.close()
        return message.value
