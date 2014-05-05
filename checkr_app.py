from flask import Flask, request
from flask_sslify import SSLify
import json
from checkr import build_response

app = Flask(__name__)
sslify = SSLify(app)


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/check', methods=['POST'])
def check():
    response_dict = build_response(request.form['inputUsername'],
        request.form['inputPassword'],
        request.form['provider'])
    return json.dumps(response_dict)