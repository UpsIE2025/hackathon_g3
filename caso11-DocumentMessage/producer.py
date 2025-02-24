from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

# Configurar Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializa JSON a bytes
)

TOPIC_NAME = 'document_messages'

@app.route('/send-document', methods=['POST'])
def send_document():
    try:
        data = request.json  # Recibe JSON desde Postman
        if not data:
            return jsonify({"error": "No se recibió ningún documento"}), 400

        producer.send(TOPIC_NAME, data)  # Enviar mensaje a Kafka
        return jsonify({"message": "Documento enviado a Kafka", "data": data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
