#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: MicroFilm 
# Software: PyCharm
# Time    : 2018-09-28 16:36
# File    : models.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root@Tqtl911!@#)^:3306/MicroFilm/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    """
    会员表;
    """
    __tablename__ = "user"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100), unique=True)  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符
    userlogs = db.relationship("UserLog", backref="user")  # 会员日志外键关联
    comments = db.relationship("Comment", backref="user")  # 评论外键关联
    moviecols = db.relationship("MovieCol", backref="user")  # 收藏外键关联

    def __repr__(self):
        return "<User %r>" % self.name


class UserLog(db.Model):
    """
    会员登录日志表;
    """
    __tablename__ = "userlog"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 登录时间；

    def __repr__(self):
        return "<UserLog %r>" % self.id


class Tag(db.Model):
    """
     标签表;
    """
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    movies = db.relationship("Movie", backref="tag")  # 电影外键关系的关联

    def __repr__(self):
        return "<Tag %r>" % self.name


class Movie(db.Model):
    """
    电影表;
    """
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 地址
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))  # 所属标签
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.Date)  # 上映时间
    length = db.Column(db.String(100))  # 播放时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    comments = db.relationship("Comment", backref="movie")  # 评论外键关系关联
    moviecols = db.relationship("MovieCol", backref="movie")  # 收藏外键关系关联

    def __repr__(self):
        return "<Movie %r>" % self.title


class Preview(db.Model):
    """
    上映预告表;
    """
    __tablename__ = "preview"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    logo = db.Column(db.String(255), unique=True)  # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Preview %r>" % self.title


class Comment(db.Model):
    """
    评论表;
    """
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 内容
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Comment %r>" % self.id


class MovieCol(db.Model):
    """
    电影收藏表;
    """
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<MovieCol %4>" % self.id
