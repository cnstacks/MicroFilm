#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MicroFilm 
# Software: PyCharm
# Time    : 2018-09-28 16:36
# File    : __init__.py.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Flask

app = Flask(__name__)

app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
