#!usr/bin/python3
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/echo', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "get request"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"

if __name__ == '__main__':
    app.run(host='0.0.0.0')