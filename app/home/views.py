#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MicroFilm 
# Software: PyCharm
# Time    : 2018-09-28 16:38
# File    : views.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from . import home
from flask import render_template, redirect,url_for


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/login/")
def login():
    return render_template("home/login.html")


@home.route("/logout")
def logout():
    return redirect(url_for("home.login"))