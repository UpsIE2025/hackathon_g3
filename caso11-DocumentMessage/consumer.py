from kafka import KafkaConsumer
import redis
import json

# Configurar Kafka Consumer
consumer = KafkaConsumer(
    'document_messages',  # Nombre del tópico
    bootstrap_servers='localhost:9092',  # Dirección de Kafka
    auto_offset_reset='earliest',  # Leer desde el primer mensaje
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))  # Deserializar JSON a Python
)

# Configurar Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

print("Esperando documentos desde Kafka...")

for message in consumer:
    # Recibir el documento JSON
    document = message.value
    print(f"📄 Documento recibido: {document}")

    # Verificar si el documento contiene el campo "productos"
    if 'productos' in document:
        # Sumar las cantidades de productos
        total_cantidad = sum(producto['cantidad'] for producto in document['productos'])
        print(f"Total de productos: {total_cantidad}")

        # Agregar el total de productos al documento
        document['total_cantidad'] = total_cantidad

        # Serializar el documento a JSON (convertir a cadena)
        document_json = json.dumps(document)

        # Almacenar el documento completo en Redis
        document_id = f"doc:{message.offset}"  # Genera un ID único usando el offset del mensaje
        redis_client.set(document_id, document_json)  # Guardar el documento completo en Redis
        redis_client.set(f"{document_id}:total_cantidad", total_cantidad)  # Guardar el total de productos en Redis

        print(f"✅ Documento almacenado en Redis con clave {document_id} y total de productos {total_cantidad}")
    else:
        print("❌ El mensaje no contiene el campo 'productos'.")
