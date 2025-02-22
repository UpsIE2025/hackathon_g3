from flask import Flask, jsonify
from kafka import KafkaConsumer
import redis
import json
import threading
import time

# Configuración de Kafka y Redis
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'MessageBus'
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# Crear la aplicación Flask
app = Flask(__name__)

# Conexión a Redis
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

# Conexión a Kafka
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    group_id='order_consumer_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def procesar_mensajes():
    for mensaje in consumer:
        order = mensaje.value
        print(f"Procesando mensaje: {order}")
        
        # Almacenar el mensaje procesado en Redis
        r.set(f"processed_order:{order['order_id']}", json.dumps(order))
        print(f"Orden {order['order_id']} almacenada en Redis")

@app.route('/processed_orders/<order_id>', methods=['GET'])
def obtener_orden_procesada(order_id):
    # Obtener la orden procesada de Redis
    order = r.get(f"processed_order:{order_id}")
    if not order:
        return jsonify({'error': 'Order not found'}), 404

    return jsonify(json.loads(order)), 200

if __name__ == "__main__":
    # Crear un hilo para escuchar los mensajes de Kafka en segundo plano
    threading.Thread(target=procesar_mensajes, daemon=True).start()
    
    # Ejecutar el servidor Flask
    app.run(debug=True, host='0.0.0.0', port=5001)
