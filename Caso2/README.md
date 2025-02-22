PARA EJECUTAR ESTE CASO ES NECESARIO CREAR UN  AMBIENTE DE PYTHON CON EL COMANDO
python -m venv venv 
DESPUES SE NECESITA ACCEDER AL AMBIENTE E INSTALAR LAS LIBRERIAS NECESARIAS
.\venv\Scripts\Activate
python -m pip install --upgrade pip setuptools wheel
Y DESPUES SOLAMENTE NECESITAMOS EJECUTAR NUESTRO REQUERIMIENTO ESTO PARA INSTALAR TODAS LAS LIBRERIAS NECESARIAS
pip install -r requerimiento.txt
CON ESTO PODEMOS YA LEVANTAR NUESTROS MICROS
./producer.py
./consumer_sub1.py
./consumer_sub2.py
./consumer_sub3.py
Y PROCEDEMOS A PROBAR EN POSTMAN CON UN SERVICIO POST CON:
http://localhost:5000/enviar

CON EL JSON:

{
    "id": 1,
    "mensaje": "Mensaje exclusivo Subscriber 22",
    "destinatarios": ["subscriber2"]
}