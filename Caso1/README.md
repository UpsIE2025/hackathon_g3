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
---------------------------------------
#comandos ejucion
pip install kafka-python flask
python -m venv venv 
.\venv\Scripts\Activate
python -m pip install --upgrade pip setuptools wheel
pip install kafka-python redis
pip install Flask kafka-python redis
---------------------------------------
#Postman:
Método: POST
URL: http://localhost:5000/enviar
Body (JSON):
{
  "id": 1,
  "contenido": "Hola desde Kafka"
}
---------------------------------------