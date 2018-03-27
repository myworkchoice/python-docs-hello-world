from flask import Flask
from flask import make_response
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
  # Set up the parameters we want to pass to the API.
  # This is the latitude and longitude of New York City.
  parameters = {"lat": 40.71, "lon": -74}

  # Make a get request with the parameters.
  #response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

  # Print the content of the response (the data the server returned)
  #print(response.content)

  # This gets the same data as the command above
  response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
  return  (response.content)

if __name__ == '__main__':
  app.run()
