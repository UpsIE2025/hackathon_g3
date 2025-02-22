from flask import Flask, request, jsonify
import redis
import json

class MensajeAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

        # Definir rutas
        self.app.add_url_rule('/mensajes', 'recibir_mensaje', self.recibir_mensaje, methods=['POST'])
        self.app.add_url_rule('/mensajes_invalidos', 'obtener_mensajes_invalidos', self.obtener_mensajes_invalidos, methods=['GET'])

    def recibir_mensaje(self):
        data = request.json
        if not data or "id" not in data or not data.get("texto"):
            self.redis_client.lpush("mensajes_invalidos", json.dumps(data))
            return jsonify({"status": "error", "message": "Mensaje inválido almacenado"}), 400
        return jsonify({"status": "success", "message": "Mensaje válido recibido"}), 200

    def obtener_mensajes_invalidos(self):
        mensajes = self.redis_client.lrange("mensajes_invalidos", 0, -1)
        return jsonify([json.loads(m) for m in mensajes])

    def run(self):
        self.app.run(debug=True, port=5000)

if __name__ == '__main__':
    api = MensajeAPI()
    api.run()
