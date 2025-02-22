from redis import Redis
import json
import time

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

def redis_consumer():
    redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    while True:
        _, msg = redis_client.brpop('mensajes')
        msg = json.loads(msg)
        print(f"[Consumer-Redis] Procesado desde Redis: {msg}")
        time.sleep(2)

if __name__ == "__main__":
    redis_consumer()
