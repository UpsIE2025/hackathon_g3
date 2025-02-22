from flask import Flask, jsonify, request
from kafka import KafkaConsumer, KafkaProducer
import json

app = Flask(__name__)

consumer = KafkaConsumer(
    'dead_letter_channel',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/dead_messages', methods=['GET'])
def obtener_mensajes_fallidos():
    dead_messages = []
    
    for message in consumer:
        dead_messages.append(message.value)
    
    return jsonify({"dead_messages": dead_messages})

@app.route('/retry', methods=['POST'])
def reintentar_mensaje():
    data = request.json
    message = data.get("message")
    original_topic = message.get("failed_topic")

    if not message:
        return jsonify({"error": "Mensaje inválido"}), 400

    producer.send(original_topic, message["original_message"])
    producer.flush()
    return jsonify({"mensaje": "Mensaje reenviado correctamente"}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
