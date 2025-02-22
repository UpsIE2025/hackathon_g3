#creacion del topic
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic Datatype

 pip install kafka-python
 pip install flask kafka-python redis
 pip install flask    
 python -m venv .venv

 docker-compose up -d    
 Ejcutar proyecto:
  Abrir dos terminales
  python productor.py
  python comsumidor.py

  Ejecutar principal
  python principal.py

Estructura: 
  Caso1
   -consumidor.py
   -productor.py
   -principal.py

Historia de Usuario:

Título: Selección de canal por tipo de datos

Como remitente o receptor de datos
Quiero que los canales de comunicación estén separados por tipo de datos
Para que se garantice que todos los datos en un canal sean del mismo tipo y se facilite la identificación de los datos tanto para el remitente como para el receptor.

Criterios de Aceptación:

1. Canales separados por tipo de datos:

- Existen canales diferentes para cada tipo de datos (por ejemplo: texto, imágenes, videos, documentos).
- Los datos en cada canal deben ser del tipo específico para el que está diseñado.

2. Selección de canal por parte del remitente:

- El remitente debe tener la opción de seleccionar el canal adecuado basado en el tipo de datos que está enviando (si es texto, imágenes, videos, etc.).
- El remitente deberá conocer el tipo de datos que está enviando y seleccionar el canal correspondiente.

3. Identificación de tipo de datos para el receptor:

- El receptor debe conocer el tipo de los datos que está recibiendo basándose en el canal en el que fueron enviados.
- Los canales deben estar claramente etiquetados o identificados para que tanto el remitente como el receptor sepan cuál es el tipo de datos en cada canal.
4. Mensajes de error o advertencias:

- Si un remitente intenta enviar un tipo de datos incorrecto por un canal, debe recibir un mensaje de error o advertencia.
- El receptor debe ser capaz de detectar si los datos recibidos no corresponden al tipo esperado, y debe recibir una alerta en caso de inconsistencias.

5. Ejemplo de uso:

Si un remitente envia un mensaje con informacion del cliente, ahora el receptor para obtener la informacion deberia conocer el Id para poder obtener la informacion.

Postman:
POST: http://localhost:5000/send_message
  RAW 
  {
  "id_cliente": "10",
  "nombre": "Grupo 3",
  "edad": 1,
  "promocion": "20% de descuento"
}

Resultado: 
{
    "message": "Mensaje enviado a Kafka y almacenado en Redis",
    "status": "success"
}

GET: http://localhost:5000/get_message/10
{
    "message": {
        "edad": 1,
        "id_cliente": "10",
        "nombre": "Grupo 3",
        "promocion": "20% de descuento"
    },
    "status": "success"
}

GET: http://localhost:5000/consume_message
{
    "message": {
        "edad": 1,
        "id_cliente": "10",
        "nombre": "Grupo 3",
        "promocion": "20% de descuento"
    },
    "status": "success"
}


