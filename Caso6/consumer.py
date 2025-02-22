import redis
from kafka import KafkaConsumer
 
# Configurar Redis y Kafka
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
consumer = KafkaConsumer('guaranteed-delivery', bootstrap_servers='localhost:9092')
 
print("Esperando mensajes...")
 
for message in consumer:
    received_message = message.value.decode()
    print(f"Mensaje recibido: {received_message}")
 
    # Eliminar el mensaje de Redis solo después de procesarlo
    for key in redis_client.keys("msg:*"):
        if redis_client.get(key) == received_message:
            redis_client.delete(key)
            print(f"Mensaje eliminado de Redis: {received_message}")