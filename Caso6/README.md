Definir un tópico de Kafka
kafka-topics.sh --create --topic guaranteed-delivery-topic --bootstrap-server localhost:9092 --partitions 3
--caso 6


HISTORIA DE USUARIO

Técnica: Entrega Garantizada de Mensajes en Transacciones Bancarias

Título:Garantizar la entrega segura de transacciones bancarias entre sistemas distribuidos.

Como: Un sistema de procesamiento de pagos bancarios.

Quiero:Que cada transacción enviada desde el sistema de pagos a la base de datos central sea almacenada de manera persistente en cada punto intermedio, de modo que, si ocurre una falla en el sistema de mensajería, la transacción no se pierda.

Para que: Pueda garantizar la integridad y consistencia de las transacciones bancarias sin riesgo de pérdida de datos.


CRITERIOS DE ACEPTACION

Entrega Única del Mensaje
    DADO que un mensaje de promoción se publica en Kafka,
    CUANDO múltiples consumidores intentan procesarlo,
    ENTONCES solo un consumidor debe recibir y manejar ese mensaje.

Registro y Control de Entrega con Redis
    DADO que un mensaje es recibido por un consumidor,
    CUANDO se verifica el ID del cliente en Redis,
    ENTONCES si el mensaje ya fue procesado, se descarta; si no, se marca como entregado.

Selección del Canal Adecuado
    DADO que un cliente tiene múltiples canales disponibles (Email, SMS, WhatsApp),
    CUANDO un mensaje es procesado,
    ENTONCES el sistema debe seleccionar el canal prioritario basado en reglas de negocio.

Reintento en Caso de Falla
    DADO que un mensaje fue enviado a un canal,
    CUANDO no se recibe confirmación de entrega en X tiempo,
    ENTONCES el mensaje se reenvía por otro canal disponible.

Monitoreo y Reporte
    DADO que la campaña está en ejecución,
    CUANDO se procesan mensajes,
    ENTONCES el sistema debe generar métricas de envíos, entregas y fallos en un dashboard.


✅ Cola de respaldo: Redis puede actuar como un buffer si Kafka tiene problemas.
✅ Cacheo de mensajes: Redis puede almacenar temporalmente los mensajes antes de enviarlos a Kafka.
✅ Duplicación de mensajes: Redis puede ayudar a evitar que los consumidores procesen mensajes duplicados.
🚀 Con Redis
Si quieres asegurar aún más la entrega garantizada, puedes modificar producer.py para almacenar los mensajes en Redis antes de enviarlos a Kafka.
Instalar Redis y la librería Python
Modificar producer.py Ejecutar el Código en Python
Sigue estos pasos:
 
2️⃣ Ejecutar el Productor Flask
python producer.py
3️⃣ Ejecutar el Consumidor
python consumer.py
4️⃣ Probar con Postman
Envia un POST a http://localhost:5000/send con:
{"message": "Prueba con Redis y Kafka"}
5️⃣ Ver los mensajes en Kafka
Corre el consumidor (consumer.py) y revisa la salida en la terminal.
tiene menú contextual