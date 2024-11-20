
from flask import Flask, jsonify, request

app = Flask(__name__)

message = "hello world"

# Route to get message
@app.route('/hello_world', methods=['GET'])
def get_messages():
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=42069)
