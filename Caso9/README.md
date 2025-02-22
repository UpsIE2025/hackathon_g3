#creacion del topic
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic MessageBus
pip install kafka-python
 pip install flask kafka-python redis
 pip install flask    
 python -m venv .venv

Ejecucion:
1:
python productor.py
2:
python consumidor.py

Historia de Usuario
Título: Comunicación entre aplicaciones mediante el Message Bus

Como: Usuario o sistema que necesita interactuar con diferentes aplicaciones en un ecosistema,
Quiero: Utilizar un Message Bus para que las aplicaciones puedan intercambiar mensajes de forma eficiente y sin necesidad de integración directa,
Para que: Las aplicaciones trabajen juntas y compartan información de manera confiable y escalable.

Criterios de aceptación:
1. Comunicación desacoplada: Las aplicaciones no deben depender directamente de otras aplicaciones, solo del Message Bus para la comunicación.

2. Interfaz común: El sistema debe proveer un conjunto común de comandos y mensajes para permitir la comunicación entre diferentes aplicaciones.

3. Escalabilidad: El Message Bus debe ser capaz de manejar una cantidad creciente de mensajes a medida que las aplicaciones crecen o se expanden.

4. Fiabilidad: Los mensajes enviados entre las aplicaciones deben ser entregados de manera confiable, incluso en caso de fallos en algunas aplicaciones o componentes.

5. Seguridad: El Message Bus debe garantizar la seguridad de los datos que se comunican, con encriptación y autenticación de los mensajes.

6. Manejo de errores: El sistema debe contar con mecanismos para manejar fallos de mensajes, tales como reintentos o notificaciones de error a los administradores.

Ejemplo:
Dado que una aplicación de ventas necesita comunicar la información de las compras a la aplicación de inventarios y la de facturación,
Cuando un cliente realiza una compra,
Entonces el sistema de ventas debe enviar un mensaje al Message Bus con los detalles de la compra,
Y las aplicaciones de inventario y facturación deben recibir el mensaje y actualizar sus datos de manera adecuada sin depender directamente de la aplicación de ventas.

En estes caso se consume por Id


Postman
POST: http://localhost:5000/produce
{
    "message": "Mensaje enviado a Kafka",
    "order": {
        "order_id": "123458",
        "price": 1200.0,
        "product": "Laptop",
        "quantity": 1,
        "timestamp": 1740246230.3059227
    }
}

GET: http://localhost:5001/processed_orders/123458

{
    "order_id": "123458",
    "price": 1200.0,
    "product": "Laptop",
    "quantity": 1,
    "timestamp": 1740246230.3059227
}



