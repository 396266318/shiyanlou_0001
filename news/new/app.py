#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from datetime import datetime
from pymongo import MongoClient
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event

app = Flask(__name__)


# app.config.update(
#     {'SQLALCHEMY_DATABASE_URI': 'mysql://root@localhost/news'})
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='mysql://huxin:l1hg5JdhezWf@192.168.6.68:3306/shiyanlou'))
# db.init_app(app)

db = SQLAlchemy(app)

mongo = MongoClient('localhost', 27017).news


class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    content = db.Column(db.Text)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.relationship('Category', uselist=False)

    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def add_tag(self, tag):
        mongo.file.update_one({'_id': self.id}, {'$addToSet': {'tags': tag}})
        return self.__file['tags']

    def remove_tag(self, tag):
        mongo.file.update_one({'_id': self.id}, {'$pull': {'tags': tag_name}})
        return self.__file['tags']

    @property
    def __file(self):
        return mongo.file.find_one({'_id': self.id})

    @property
    def tags(self):
        return self.__file['tags']

@event.listens_for(File, 'after_insert')
def auto_create_mongodb_file(mapper, conn, file):
    mongo.file.insert_one({'_id': file.id})


@event.listens_for(File, 'after_delete')
def auto_delete_mongodb_file(mapper, conn, file):
    mongo.file.delete_one({'_id': file.id})


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')

    def __init__(self, name):
        self.name = name


@app.route('/')
@app.route('/files/')
def index():
    return render_template('index.html', files=File.query.all())


@app.route('/files/<int:file_id>')
def file(file_id):
    file = File.query.get_or_404(file_id)
    return render_template('file.html', file=file)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


def insert_datas():
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')


if __name__ == '__main__':
    db.create_all()
    if not Category.query.filter_by(name='Java').first():
        insert_datas()
    app.run()
