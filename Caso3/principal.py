from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
import redis
import json

app = Flask(__name__)

# Configuración de Kafka
KAFKA_SERVER = 'localhost:9092'  # Dirección del servidor Kafka
TOPIC_NAME = 'usuario_topic'  # Nombre del topic Kafka donde se enviarán los mensajes

# Configuración de Redis
REDIS_SERVER = 'localhost'  # Dirección del servidor Redis
REDIS_PORT = 6379  # Puerto de Redis
REDIS_DB = 0  # Base de datos de Redis

# Conexión a Kafka (Productor)
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializar los mensajes en JSON
)

# Conexión a Redis
r = redis.Redis(host=REDIS_SERVER, port=REDIS_PORT, db=REDIS_DB)

@app.route('/send_message', methods=['POST'])
def send_message():
    """Endpoint para enviar un mensaje a Kafka y almacenarlo en Redis"""
    try:
        # Obtener los datos del cuerpo de la solicitud
        data = request.get_json()

        # Enviar el mensaje a Kafka
        producer.send(TOPIC_NAME, data)
        producer.flush()

        # Almacenar el mensaje en Redis
        r.set(data['id_cliente'], json.dumps(data))

        return jsonify({"status": "success", "message": "Mensaje enviado a Kafka y almacenado en Redis"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


@app.route('/get_message/<client_id>', methods=['GET'])
def get_message(client_id):
    """Endpoint para obtener un mensaje de Redis por el id_cliente"""
    try:
        # Buscar el mensaje en Redis usando el id_cliente
        message = r.get(client_id)
        
        if message:
            return jsonify({"status": "success", "message": json.loads(message)}), 200
        else:
            return jsonify({"status": "error", "message": "Mensaje no encontrado en Redis"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


@app.route('/consume_message', methods=['GET'])
def consume_message():
    """Endpoint para consumir mensajes de Kafka"""
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_SERVER,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # Deserializar los mensajes JSON
    )
    
    for message in consumer:
        # Devolver el primer mensaje consumido de Kafka (puedes ajustar esto para consumir más mensajes)
        consumer.close()
        return jsonify({"status": "success", "message": message.value}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
