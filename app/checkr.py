from flask import Flask, request, render_template
import json
from checkr_app import build_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('form_page.html')


@app.route('/images/<name>')
def image(name):
    return 'Image is ' + name


@app.route('/check', methods=['POST'])
def check():
    response_dict = build_response(request.form['inputUsername'],
        request.form['inputPassword'],
        request.form['provider'])
    return render_template('results.html', response_dict=response_dict)

if __name__ == '__main__':
    app.run(debug=True)
