#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MicroFilm 
# Software: PyCharm
# Time    : 2018-09-28 16:37
# File    : __init__.py.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Blueprint
home = Blueprint("home",__name__)
import app.home.views


