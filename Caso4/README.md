poreviamente debe estar ejecutado el docker compose up

#comandos de instalacion
pip install kafka-python flask
python -m venv venv 
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
pip install kafka-python redis
pip install Flask kafka-python redis
pip install kafka-python redis

#abrir dos terminales
python valid_consumer.py  # Terminal 1
python invalid_consumer.py  # Terminal 2

#abrir un tercer terminal
python publisher.py

#verificar consumer valido
python valid_consumer.py

#verificar consumer invalido
python invalid_consumer.py
