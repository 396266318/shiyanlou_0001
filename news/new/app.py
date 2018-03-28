# -*- coding:utf-8 -*-
from flask import Flask
from flask import render_template, redirect, url_for, abort
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.update({'SECRET_KEY': 'a random string'})
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://huxin:l1hg5JdhezWf@192.168.6.68:3306/shiyanlou'

db = SQLAlchemy(app)


class File(db.Model):
    __tablename__ = 'file' # 文件表
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category')  # 实例化 Category 关系

    def __init__(self, title, created_time, category_id, content):
        self.title = title
        # if created_time is None:
        #     created_time = datetime.utcnow()
        self.created_time = created_time
        self.category_id = category_id
        self.content = content

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


@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示 files 目录下所有的json 文件中的 title 信息列表
    return render_template('index.html', title=File.query.all())


@app.route('/files/<file_id>')
def file(file_id):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 'shiyanlou 404' 404 错误页面

    # if filename == 'helloshiyanlou':
    #     content = {
    #         'title1': new1.title,
    #         'created_time1': new1.created_time,
    #         'content1': new1.content,
    #         'type1': new1.category
    #     }
    #     return render_template('file.html', content=content)
    # elif filename == 'helloworld':
    #     content = {
    #         'title2': new2.title,
    #         'created_time2': new2.created_time,
    #         'content2': new2.content,
    #         'type2': new2.category,
    #     }
    #     return render_template('file.html', content=content)

    # else:
    #     abort(404)
    file_items = File.query.get_or_404(file_id)

    return render_template('file.html', items=file_items)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, port=3000)
