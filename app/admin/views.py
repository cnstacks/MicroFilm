#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MicroFilm 
# Software: PyCharm
# Time    : 2018-09-28 16:38
# File    : views.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from . import admin


@admin.route("/")
def index():
    return "<h1 style='color:yellow'>This is admin Blueprint<h1>"
