# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 20:15:30 2020

@author: nyamochir bold
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world!"
