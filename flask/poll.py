#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""
Simple poll app
"""

from flask import Flask, render_template

poll = [{"question" : "
        {"choice" ; "choice 1", "count" : 0 },
        {"choice" : "choice 2", "count" : 0 },
        {"choice" : "choice 3", "count" : 0 }]

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"]
def index():
    return render_template("poll.html")



if __name__ == "__main__":
    app.run(debug=True)
