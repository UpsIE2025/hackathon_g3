from flask import Flask, request, jsonify
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import json

app = Flask(__name__)

KAFKA_TOPIC = 'point_to_point_topic'
KAFKA_SERVER = 'localhost:9092'

# 🚀 Crear el tópico si no existe
def crear_topico():
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_SERVER,
        client_id='admin_client'
    )
    topics = admin_client.list_topics()
    if KAFKA_TOPIC not in topics:
        topic_list = [NewTopic(name=KAFKA_TOPIC, num_partitions=1, replication_factor=1)]
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(f"✅ Tópico '{KAFKA_TOPIC}' creado exitosamente.")
    else:
        print(f"ℹ️ El tópico '{KAFKA_TOPIC}' ya existe.")

# 🌐 Configurar el productor Kafka
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/enviar', methods=['POST'])
def enviar_mensaje():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400
    
    producer.send(KAFKA_TOPIC, data)
    producer.flush()
    return jsonify({"status": "Mensaje enviado", "mensaje": data}), 200

if __name__ == "__main__":
    crear_topico()  # 💡 Crea el tópico al iniciar
    app.run(host='0.0.0.0', port=5000, debug=True)