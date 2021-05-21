# -*- coding: utf-8 -*-
"""
Created on Thu May 20 19:33:17 2021

@author: danny
"""

#!/usr/bin/env python
# encoding: utf-8
import json
import sys
from flask import Flask, request, jsonify

# creating a Flask app
# location is http://127.0.0.1:5000/
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/"location of json file"
@app.route('/<string:json_location>', methods=['PUT'])
def change_string(json_location):
    with open(json_location, 'r') as jsonFile:
        data = json.load(jsonFile)
    if type(data) == str:
        #reverses string
        txt = data[::-1]
    else:
        #if the json body isn't a string, sys exit
        sys.exit("not a string json body")
    with open(json_location, 'w') as jsonFile:
        json.dumps(txt, jsonFile)
    return jsonify(txt)

app.run(debug=True)