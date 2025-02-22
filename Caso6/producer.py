import redis
from flask import Flask, request, jsonify
from kafka import KafkaProducer
 
app = Flask(__name__)
 
# Configurar Kafka y Redis
producer = KafkaProducer(bootstrap_servers='localhost:9092', acks='all')
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
 
@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get('message', '')
 
    if not message:
        return jsonify({'error': 'Message cannot be empty'}), 400
 
    # Guardar mensaje en Redis antes de enviarlo a Kafka
    message_id = f"msg:{redis_client.incr('msg_id')}"
    redis_client.set(message_id, message)
 
    # Enviar mensaje a Kafka
    producer.send('guaranteed-delivery', message.encode('utf-8'))
    producer.flush()
 
    return jsonify({'status': 'Message stored in Redis and sent to Kafka'}), 200
 
if __name__ == '__main__':
    app.run(debug=True, port=5000)