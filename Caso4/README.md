Historia de Usuario: Manejo de Mensajes Inválidos en Procesamiento de Facturas
Título:
Como sistema de procesamiento de facturas, quiero mover los mensajes con errores a un canal de mensajes no válidos para evitar fallos en el sistema principal.

Descripción:
Una empresa de contabilidad procesa facturas electrónicas enviadas por diferentes clientes. Las facturas llegan en formato JSON a un sistema de mensajería, donde se validan antes de ser almacenadas en la base de datos. Si una factura contiene errores de estructura, datos incorrectos o valores fuera de rango, debe moverse automáticamente a un canal de mensajes no válidos para su posterior análisis y corrección, sin afectar el flujo normal del procesamiento.

Criterios de Aceptación:

Validación de Mensajes: Si el mensaje recibido no cumple con el formato esperado, se debe marcar como inválido.
Movimiento Automático: El sistema debe mover automáticamente los mensajes inválidos a un canal especial para evitar que interrumpan el procesamiento.
Registro de Errores: Cada mensaje inválido debe registrar la razón del fallo en un sistema de logs para diagnóstico.
Notificación: Se debe notificar a los administradores cuando un mensaje se mueva al canal de mensajes no válidos.
Recuperación Manual: Los mensajes inválidos deben poder ser revisados y reenviados manualmente tras la corrección.


------------------------------------------------------------------------------------------------------------
-- PASOS DE EJCUCION
------------------------------------------------------------------------------------------------------------
#previamente debe estar ejecutado el docker compose up

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
