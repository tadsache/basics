
from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__)
metrics = PrometheusMetrics(app)

message = "hello world"

# Route to get message
@app.route('/hello_world', methods=['GET'])
def get_messages():
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=42069)


