#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MicroFilm 
# Software: PyCharm
# Time    : 2018-09-28 16:29
# File    : app.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1 style = 'color:red'>Hello Flask!</h1>"


if __name__ == '__main__':
    app.run()
