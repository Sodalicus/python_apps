#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""

"""

import requests

payload = dict(xxx='value1', yyy='value2')
r = requests.post('http://127.0.0.1:5000/incoming', data=payload)

