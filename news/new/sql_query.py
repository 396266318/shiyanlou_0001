#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy import Session
from datetime import datetime


app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://huxin:l1hg5JdhezWf@192.168.6.68:3306/shiyanlou'

db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = 'category' # 类别表
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repy__(self):
        return 'Category {0}'.format(self.name)


class File(db.Model):
    __tablename__ = 'file' # 文件表
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category_id'))
    content = db.Column(db.Text)

    def __init__(self, title, created_time, category_id, content):
        self.title = title
        # if created_time is None:
        #     created_time = datetime.utcnow()
        self.created_time = created_time
        self.category_id = category_id
        self.content = content

    def __repr__(self):
        return 'File{0}'.format(self.username)


# if __name__ == "__main__":
    # db.create_all()
    # java = Category('Java')
    # python = Category('Python')
    # file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    # file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - python is cool!')
    # db.session.add(java, python, file1, file2)
    # db.session.commit()