from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route('/kafka', methods=['POST'])

def kafka():
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)