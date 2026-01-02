# flask-app.py
from flask import Flask, request
from flask_cors import CORS
import json
import time

# create a Flask instance
app = Flask(__name__)
# Configure CORS
# This will allow requests from http://localhost:4200 to all routes
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})
# Load configuration from config.json
print(f"flask-api.py is opening config.json to load the configuration")   
with open('config.json') as config_file:
    config = json.load(config_file)

app.config.update(config)

# a simple description of the API written in html.
# Flask can print and return raw text to the browser. 
# This enables html, json, etc. 

description =   """
                <!DOCTYPE html>
                <head>
                <title>API Landing</title>
                </head>
                <body>  
                    <h3>A simple API using Flask</h3>
                    <p>DDBB-SERVER: {db_server}</p>
                    <p>API_PORT: {port}</p>
                    <a href="http://localhost:{port}/api?value=2">sample request</a>
                </body>
                """.format(db_server=app.config.get('DDBB-SERVER'), port=app.config.get('API-PORT'))
				
# Routes refer to url'
# our root url '/' will show our html description
@app.route('/', methods=['GET'])
def hello_world():
    # return a html format string that is rendered in the browser
	return description

# our '/api' url
# requires user integer argument: value
# returns error message if wrong arguments are passed.
@app.route('/api', methods=['GET'])
def square():
    if not all(k in request.args for k in (["value"])):
        # we can also print dynamically 
        # using python f strings and with 
        # html elements such as line breaks (<br>)
        error_message = (
            f"Required paremeters : 'value'<br>"
            f"Supplied paremeters : {[k for k in request.args]}"
        )
        return error_message
    else:
        # assign and cast variable to int
        value = int(request.args['value'])
        # or use the built in get method and assign a type
        # http://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.MultiDict.get
        value = request.args.get('value', type=int)
        time.sleep(10)
        return json.dumps({"description": "Value Squared", "value": value**2})

if __name__ == "__main__":
	# for debugging locally
	# app.run(debug=True, host='0.0.0.0',port=app.config.get('API-PORT'))
	
	# for production
	app.run(host='0.0.0.0', port=app.config.get('API-PORT'))