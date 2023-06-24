#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""

echo server
"""

from flask import Flask
from flask import request

app = Flask(__name__)
data="test"

@app.route("/")
def echo_response():
    #return "<p>Hello, World!</p>"
    return data

@app.route("/incoming", methods = ["POST"])
def incoming_data():
    global data
    if request.method == "POST":

        print("type", type(request.form))
        data = request.form

        if "xxx" and "yyy" in data.keys():
            print(data.keys())
            print(data.values())
            return "OK"
        else:
            return "KO"

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
