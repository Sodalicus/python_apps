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

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"]
