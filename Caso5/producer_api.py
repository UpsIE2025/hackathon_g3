from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import random

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPICS = {
    "orders": "orders_channel",
    "dead_letter": "dead_letter_channel"
}

@app.route('/enviar', methods=['POST'])
def enviar_mensaje():
    data = request.json
    topic = TOPICS["orders"]

    try:
        # Simular fallo aleatorio para pruebas
        if random.random() < 0.2:  
            raise Exception("Error simulado en entrega")

        producer.send(topic, data)
        producer.flush()
        return jsonify({"mensaje": "Mensaje enviado", "data": data}), 200

    except Exception as e:
        # Mover mensaje al Dead Letter Channel
        dead_message = {
            "original_message": data,
            "error": str(e),
            "failed_topic": topic
        }
        producer.send(TOPICS["dead_letter"], dead_message)
        producer.flush()
        return jsonify({"error": "Mensaje fallido, movido a Dead Letter Channel"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)