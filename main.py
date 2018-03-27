from flask import Flask, jsonify
from flask import make_response
from flask import request
import json

app = Flask(__name__)

shift = [
    {
        'id': '5ab5c822ec51f60988318e17',
        'title': 'Coffe Maker',
        'startdate': '20180326',
        'Active': False
    },
    {
        'id': '5ab5c822ec51f60988319e17',
        'title': 'Marketing Officer',
        'startdate': '20180329',
        'Active': True
    }
]


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 500)

@app.route('/api/v1.0/shift')
def get_shifts():
    input = request.args.get('shiftin')
    output = json.loads(input)

    if 'firstName' in output:
        shiftid= output['firstName']
        return jsonify(
        {'firstName': shiftid})

    else:
        return jsonify(
            {'Shift':output})
        print(shift)
        print(shiftid)



if __name__ == '__main__':
    app.run()
