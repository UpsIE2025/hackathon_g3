#creacion de un venv
python3 -m venv venv
#activacionvenv
source venv/bin/activate
#abrir dos terminales
python valid_consumer.py  # Terminal 1
python invalid_consumer.py  # Terminal 2
#abrir un tercer terminal
python publisher.py
#verificar consumer valido
python valid_consumer.py
#verificar consumer invalido
python invalid_consumer.py
