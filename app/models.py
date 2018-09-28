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
from datetime import datetime
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Tqtl911!@#)^@localhost:3306/MicroFilm"
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
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
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
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 登录时间；

    def __repr__(self):
        return "<UserLog %r>" % self.id


class Tag(db.Model):
    """
     标签表;
    """
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
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
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
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
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

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
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

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
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<MovieCol %4>" % self.id


class Auth(db.Model):
    """
    权限表;
    """
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Auth %r>" % self.name


class Role(db.Model):
    """
    角色表;
    """
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(600))  # 权限
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间

    def __repr__(self):
        return "<Role %r>" % self.name


class Admin(db.Model):
    """
    管理员表;
    """
    __tablename__ = "admin"  # 表名
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100), unique=True)  # 密码
    is_super = db.Column(db.SmallInteger)  # 是否为超级管理员，0为超级管理员；
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))  # 所属角色
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 添加时间
    adminlogs = db.relationship("AdminLog", backref="admin")  # 管理员登录日志
    oplogs = db.relationship("OpLog", backref="admin")  # 操作日志

    def __repr__(self):
        return "<Admin %r>" % self.name


class AdminLog(db.Model):
    """
    管理员登录日志表;
    """
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<AdminLog %r>" % self.id


class OpLog(db.Model):
    """
    操作日志表;
    """
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey("admin.id"))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    reason = db.Column(db.String(600))  # 操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间;

    def __repr__(self):
        return "<OpLog %r>" % self.id


if __name__ == '__main__':
    db.create_all()
    """
    role = Role(
        name="超级管理员",
        auths="",
    )
    db.session.add(role)
    db.session.commit()
    """
# from werkzeug.security import generate_password_hash
#
# admin = Admin(
#     name="ImoocMovie1",
#     pwd=generate_password_hash("ImoocMovie1"),
#     is_super=0,
#     role_id=1
# )
# db.session.add(admin)
# db.session.commit()
