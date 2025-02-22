Título: Implementación de Mensaje de Documento para Transferencia de Datos Entre Aplicaciones

Como responsable de integración de sistemas,
Quiero utilizar un mensaje de documento para transferir de forma fiable estructuras de datos entre aplicaciones,
Para que cada receptor pueda decidir cómo procesar los datos y descomponerlos en unidades más pequeñas según sus necesidades.

Criterios de Aceptación:
Fiabilidad en la Transferencia:

El mensaje de documento debe permitir la transferencia fiable de datos entre diferentes aplicaciones.
La estructura del mensaje debe ser estándar y fácil de interpretar por cualquier aplicación receptora.
Unidad de Datos:

El mensaje será una única unidad de datos (por ejemplo, un objeto o estructura de datos compleja) que encapsula la información relevante.
La unidad de datos puede contener subcomponentes que el receptor puede descomponer y procesar según sea necesario.
Descomposición de Datos:

Aunque el mensaje es una unidad completa de datos, deberá ser posible que el receptor decida si desea descomponer los datos en partes más pequeñas para realizar tareas específicas o para almacenarlas por separado.
El receptor no está obligado a descomponer los datos, pero tiene la opción de hacerlo si lo requiere.
Interoperabilidad:

El mensaje de documento debe ser compatible con diversas aplicaciones dentro de la empresa sin necesidad de modificación significativa.
Las aplicaciones deberán contar con la capacidad de crear, recibir y procesar estos mensajes de documento utilizando un protocolo común (como JSON, XML, o algún formato estandarizado).
Independencia de los Receptores:

El receptor del mensaje no necesita conocer la lógica interna de la aplicación que envió el mensaje. El mensaje es autónomo y debe contener toda la información que el receptor necesita para procesar los datos.
Si un receptor necesita hacer algo específico con los datos (como cálculos, almacenamiento o acciones en una base de datos), tiene la libertad de hacerlo sin afectar a otros receptores.

---------------------------------------------------------------------
#proceso de instalacion
---------------------------------------------------------------------
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate
pip install kafka-python redis
pip install flask kafka-python redis
python -m pip install --upgrade pip setuptools wheel


#abrimos dos terminales en cada una ejecutamos el siguiente comando
Set-ExecutionPolicy Unrestricted -Scope Process
python producer.py  # terminal 1 Inicia el servidor Flask
python consumer.py  # terminal 2 Inicia el consumidor de Kafka

---------------------------------------------------------------------
#ejecucion desde postman
---------------------------------------------------------------------
http://localhost:5000/send-document
body tipo JSON
{
    "id": 101,
    "cliente": "Empresa XYZ",
    "monto": 5000,
    "fecha": "2025-02-22",
    "productos": [
        {"nombre": "Laptop", "cantidad": 10},
        {"nombre": "Mouse", "cantidad": 10}
    ]
}

Respuesta
 Documento recibido: {'id': 101, 'cliente': 'Empresa XYZ', 'monto': 5000, 'fecha': '2025-02-22', 'productos': [{'nombre': 'Laptop', 'cantidad': 10}, {'nombre': 'Mouse', 'cantidad': 10}]}
Total de productos: 20
✅ Documento almacenado en Redis con clave doc:0 y total de productos 20