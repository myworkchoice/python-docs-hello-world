from flask import Flask, jsonify
from flask import make_response
from flask import request
import json

app = Flask(__name__)

@app.route('/api/v1.0/shift')
def get_shifts():
    return 'Hello, World!!!!!!!'

@app.route("/proxy-example")
def proxy_example():
    r = requests.get("http://example.com/other-endpoint")
    return Response(
        r.text
        status=r.status_code,
        content_type=r.headers['content-type'],
    )

if __name__ == '__main__':
    app.run()
