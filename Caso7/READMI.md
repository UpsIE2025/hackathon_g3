Historia de Usuario: Integración de Órdenes de Compra con un Channel Adapter
Título:
Como sistema de gestión de órdenes de compra, quiero integrar mis datos con otros sistemas mediante un Channel Adapter, para asegurar una comunicación eficiente y en tiempo real.

Descripción:
Una empresa de logística y distribución necesita integrar su sistema de órdenes de compra con otros sistemas internos y externos, como proveedores y sistemas de inventario.

El Channel Adapter se encargará de:
1️⃣ Leer órdenes de compra desde la API interna del sistema ERP.
2️⃣ Publicar los datos en un canal de mensajería (Kafka o RabbitMQ) para que otros sistemas los consuman.
3️⃣ Recibir respuestas de otros sistemas (confirmaciones de inventario o cambios de estado).
4️⃣ Actualizar automáticamente la orden en el ERP al recibir una respuesta.

Criterios de Aceptación:
✅ El adaptador debe extraer automáticamente las órdenes de compra desde la API del ERP y publicarlas en un canal de mensajería.
✅ Los sistemas de inventario y proveedores deben poder consumir estos mensajes para verificar stock y generar confirmaciones.
✅ El adaptador debe recibir actualizaciones del canal de mensajería y reflejar los cambios en el ERP.
✅ Debe manejar errores y reintentar envíos fallidos.
✅ Debe permitir la conexión con múltiples sistemas en paralelo sin afectar el rendimiento.

---------------------------------------------------------------------
#proceso de instalacion
---------------------------------------------------------------------
pip install kafka-python redis
pip install flask kafka-python redis
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel

#abrimos dos terminales en cada una ejecutamos el siguiente comando
Set-ExecutionPolicy Unrestricted -Scope Process
python producer.py  # terminal 1 Inicia el servidor Flask
python consumer.py  # terminal 2 Inicia el consumidor de Kafka

---------------------------------------------------------------------
#ejecucion desde postman
---------------------------------------------------------------------
http://localhost:5000/send
body tipo JSON
{
    "id": 1,
    "mensaje": "Hola desde Postman"
}

Respuesta
{
    "data": {
        "id": 1,
        "mensaje": "Hola desde Postman"
    },
    "message": "Mensaje enviado a Kafka"
}