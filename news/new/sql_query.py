import os
import json
from flask import Flask
from flask import render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
from sql_create import Category, File


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.update({
    'SECRET_KEY': 'a random string'
})
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://huxin:l1hg5JdhezWf@192.168.6.68:3306/shiyanlou'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# Category_type = Category.query.all()
# print(Category_type)

# java = Category.query.filter_by(name='Java').first()
# print(java)

title = File.query.all()
print(title)