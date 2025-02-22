import redis
import random
from kafka import KafkaConsumer, KafkaProducer

# Configurar Redis y Kafka
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
consumer = KafkaConsumer('main-topic', bootstrap_servers='localhost:9092')
dlq_producer = KafkaProducer(bootstrap_servers='localhost:9092', acks='all')

print("Esperando mensajes...")

for message in consumer:
    received_message = message.value.decode()
    print(f"Mensaje recibido: {received_message}")

    try:
        # Simular procesamiento con fallo aleatorio
        if random.choice([True, False]):  # Simula error en 50% de los casos
            raise Exception("Error al procesar mensaje")

        print(f"✅ Mensaje procesado correctamente: {received_message}")

        # Eliminar de Redis después del procesamiento exitoso
        for key in redis_client.keys("msg:*"):
            if redis_client.get(key) == received_message:
                redis_client.delete(key)
                print(f"🗑️ Mensaje eliminado de Redis: {received_message}")

    except Exception as e:
        print(f"❌ Error procesando mensaje: {received_message} - {e}")
        
        # Enviar a la Dead Letter Queue
        dlq_producer.send('dead-letter-topic', received_message.encode('utf-8'))
        dlq_producer.flush()

        # Guardar en Redis información del error
        error_id = f"error:{redis_client.incr('error_id')}"
        redis_client.hset(error_id, mapping={
            "message": received_message,
            "error": str(e),
            "machine": "Consumer1",
            "channel": "main-topic"
        })
        print(f"⚠️ Mensaje enviado a DLQ y error registrado en Redis.")
