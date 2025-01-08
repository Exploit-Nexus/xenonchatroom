import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

from flask import Flask

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=['GET'])
def hello_world():
    return "Hello, World!", 200

if __name__ == '__main__':
    app.run(debug=True)
