from flask import Flask, jsonify
from flask import make_response
from flask import request
import json

app = Flask(__name__)

@app.route('/api/v1.0/shift')
def get_shifts():
    input = request.args.get('shiftin')
    output = json.loads(input)

    if 'firstName' in output:
        return "Hello there"
    else:
        return "in else part"


if __name__ == '__main__':
    app.run()
