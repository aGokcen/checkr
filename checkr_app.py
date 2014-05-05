from flask import Flask, request, render_template
from flask_sslify import SSLify

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
    return render_template('results.html',response_dict=response_dict)