#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MicroFilm 
# Software: PyCharm
# Time    : 2018-09-28 16:38
# File    : views.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from . import admin
from flask import render_template, redirect, url_for


@admin.route("/")
def index():
    return "<h1 style='color:yellow'>This is admin Blueprint<h1>"


@admin.route("/login/")
def login():
    return render_template("admin/login.html")


@admin.route("/logout/")
def logout():
    return redirect(url_for("admin.logout"))



