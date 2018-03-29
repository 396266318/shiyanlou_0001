# -*- coding:utf-8 -*-
from datetime import datetime
from pymongo import MongoClient
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='mysql://huxin:l1hg5JdhezWf@192.168.6.68:3306/shiyanlou'))

app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config.update({'SECRET_KEY': 'a random string'})
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

db = SQLAlchemy(app)
mongo = MongoClient('192.168.32.129', 27017).shiyanlou


class File(db.Model):
    __tablename__ = 'file' # 文件表

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category', uselist=False)  # 实例化 Category 关系

    def __init__(self, title, created_time, category_id, content):
        self.title = title
        self.created_time = created_time
        self.category = category_id
        self.content = content

    def add_tag(self, tag_name):
        file_item = mongo.files.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            if tag_name not in tags:
                tags.append(tag_name)
            mongo.file.update_one({'file_id': self.id}, {'$set': {'tags': tags}})
        else:
            tags = [tag_name]
            mongo.files.insert_one({'file_id': self.id, 'tags': tags})
        return tags
    
    def remove_tag(self, tag_name):
        file_item = mongo.file.find_one({'file_id': self.id})
        if file_item:
            tags = file_item['tags']
            try:
                tags.remove(tag_name)
                new_tags = tags
            except ValueError:
                return tags
            mongo.file.update_one({'file.id': self.id}, {'$set': {'tags': new_tags}})
            return new_tags
        return []
    
    @property
    def tags(self):
        file_item = mongo.file.find_one({'file_id': self.id})
        if file_item:
            print(file_item)
            return file_item['tags']
        else:
            return []


    def __repr__(self):
        return '{0}'.format(self.title)



class Category(db.Model):
    __tablename__ = 'category' # 类别表

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repy__(self):
        return '{0}'.format(self.name)

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
    file1.add_tag('tach')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')



@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示 files 目录下所有的json 文件中的 title 信息列表
    return render_template('index.html', files=File.query.all())


@app.route('/files/<file_id>')
def file(file_id):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 'shiyanlou 404' 404 错误页面
    file_items = File.query.get_or_404(file_id)
    return render_template('file.html', file_item=file_items)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, port=3000)
