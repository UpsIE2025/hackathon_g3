---------------------------------------
Message Channel / Point to Point con Kafka
---------------------------------------

Descripción de Negocio
En un sistema distribuido, enviar un mensaje en un canal punto a punto garantiza que solo un receptor lo reciba. Apache Kafka se usa como middleware de mensajería asegurando la entrega exclusiva de mensajes a consumidores específicos.

Solo un receptor consume un mensaje determinado.
Si el canal tiene varios receptores, solo uno puede consumir con éxito.
Si varios receptores intentan consumir el mismo mensaje, Kafka garantiza que solo uno lo reciba, evitando duplicaciones.
El canal puede soportar múltiples receptores, pero solo un receptor consume cada mensaje, asegurando procesamiento exclusivo.
---------------------------------------
Criterios de Aceptación
---------------------------------------
✅ Un mensaje enviado a Kafka debe ser recibido por un solo consumidor dentro de un grupo de consumidores.
✅ Si hay varios consumidores en el mismo grupo, Kafka debe balancear la carga asegurando que solo uno procese cada mensaje.
✅ Si el consumidor asignado a un mensaje falla, Kafka debe reasignar el mensaje a otro consumidor disponible.
✅ El sistema debe ser escalable, permitiendo agregar más consumidores para procesar múltiples mensajes en paralelo.
✅ Se debe poder enviar mensajes a Kafka utilizando Postman o un cliente HTTP.
✅ Los logs deben registrar cada mensaje enviado y recibido.
---------------------------------------
Historia Técnica
---------------------------------------
Título: Implementación de mensajería punto a punto con Kafka
Descripción:
El sistema de mensajería punto a punto se implementará utilizando Apache Kafka para garantizar que un mensaje sea consumido por un solo receptor dentro de un grupo de consumidores. Esto permitirá la comunicación eficiente entre microservicios, asegurando procesamiento único de cada mensaje.
---------------------------------------
Requisitos Técnicos:
---------------------------------------
Utilizar Kafka como middleware de mensajería.
Implementar un productor que envíe mensajes a un tópico de Kafka.
Implementar un grupo de consumidores, donde solo uno procese cada mensaje.
Asegurar balanceo de carga si hay múltiples consumidores.
Manejar reintentos y reenvío en caso de fallos en el consumidor.
Exponer una API REST para enviar mensajes desde Postman.
Implementación Técnica
1️⃣ Instalar dependencias

pip install kafka-python flask

2️⃣ Crear un Productor con API REST para enviar mensajes
Crea el archivo producer_api.py:

from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/enviar', methods=['POST'])
def enviar_mensaje():
    data = request.json
    producer.send('mi-topico', data)
    producer.flush()
    return jsonify({"mensaje": "Mensaje enviado", "data": data}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
➡ Cómo probarlo en Postman:

Método: POST
URL: http://localhost:5000/enviar
Body (JSON):
json
Copiar
Editar
{
  "id": 1,
  "contenido": "Hola desde Kafka"
}
3️⃣ Crear un Consumidor que procese los mensajes
Crea el archivo consumer.py:

python
Copiar
Editar
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'mi-topico',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    group_id="grupo-consumidores"
)

print("Esperando mensajes...")

for message in consumer:
    print(f"Mensaje recibido: {message.value}")
4️⃣ Iniciar Kafka y probar

------------------------------------------------------------
1️⃣ Inicia Kafka (Si no lo tienes, instálalo y configúralo).


zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
2️⃣ Crea un tópico en Kafka


kafka-topics.sh --create --topic mi-topico --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
3️⃣ Ejecuta el consumidor primero


python consumer.py
4️⃣ Envía un mensaje desde Postman y verifica que solo un consumidor lo reciba.
