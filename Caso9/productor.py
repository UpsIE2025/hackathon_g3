from flask import Flask, jsonify, request
from kafka import KafkaProducer
import redis
import json
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
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/produce', methods=['POST'])
def producir_mensaje():
    # Obtener el cuerpo del mensaje desde la solicitud POST
    data = request.get_json()
    order_id = data.get('order_id')
    product = data.get('product')
    quantity = data.get('quantity')
    price = data.get('price')

    if not order_id or not product or not quantity or not price:
        return jsonify({'error': 'Missing required fields'}), 400

    mensaje = {
        "order_id": order_id,
        "product": product,
        "quantity": quantity,
        "price": price,
        "timestamp": time.time()
    }

    # Almacena el mensaje en Redis antes de enviarlo a Kafka (opcional)
    r.set(f'order:{order_id}', json.dumps(mensaje))

    # Enviar el mensaje a Kafka
    producer.send(KAFKA_TOPIC, mensaje)
    producer.flush()  # Asegurarse de que el mensaje se envíe

    return jsonify({'message': 'Mensaje enviado a Kafka', 'order': mensaje}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
