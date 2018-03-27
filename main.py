from flask import Flask, jsonify
from flask import make_response
from flask import request
import json

app = Flask(__name__)

@app.route('/api/v1.0/shift')
def get_shifts():
    return 'Hello, World!!!!!!!'


if __name__ == '__main__':
    app.run()
