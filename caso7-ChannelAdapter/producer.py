from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

# Configurar Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC_NAME = 'channel_adapter'

@app.route('/send', methods=['POST'])
def send_message():
    try:
        data = request.json  # Recibe JSON desde Postman
        producer.send(TOPIC_NAME, data)  # Envía el mensaje a Kafka
        return jsonify({"message": "Mensaje enviado a Kafka", "data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
