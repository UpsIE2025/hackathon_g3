#HISTORIA DE USUARIO



#creacion del topic
.\kafka-topics.sh --bootstrap-server localhost:9092 --create --topic point_to_point_topic

#comandos para ejecutar
python -m venv venv 
.\venv\Scripts\Activate
python -m pip install --upgrade pip setuptools wheel
pip install kafka-python redis
pip install Flask kafka-python redis

#conexion desde postman - metodo POST
http://localhost:5000/enviar
{
    "id": 1,
    "mensaje": "Mensaje enviado desde Postman 3"
}
