#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MicroFilm 
# Software: PyCharm
# Time    : 2018-09-28 16:36
# File    : __init__.py.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Tqtl911!@#)^@localhost:3306/MicroFilm"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'af88db871dce46cf9a68c97ed48a9892'
app.debug = True

db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404
