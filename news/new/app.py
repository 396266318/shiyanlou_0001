# -*- coding:utf-8 -*-
import os
import json
from flask import Flask
from flask import render_template, redirect, url_for, abort


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.update({
    'SECRET_KEY': 'a random string'
})


filename = 'D:/Code/files/'
file_patn = os.path.dirname(filename)
file_list = os.listdir(filename)

name = os.listdir(filename)


def file_content(filename):
    with open(filename, 'r') as file:
        content = file.read()
        file_json = json.loads(content)

        return file_json


file1 = os.path.join(file_patn, 'helloshiyanlou.json')
file2 = os.path.join(file_patn, 'helloworld.json')

file_content1 = file_content(file1)
file_content2 = file_content(file2)


@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示 files 目录下所有的json 文件中的 title 信息列表
    title = {
        'title1': file_content1.get('title'),
        'title2': file_content2.get('title')
    }

    return render_template('index.html', title=title, name=name)


@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 'shiyanlou 404' 404 错误页面

    if filename == 'helloshiyanlou':
        content = {
            'title1': file_content1.get('title'),
            'created_time1': file_content1.get('created_time'),
            'content1': file_content1.get('content'),
        }
        return render_template('file.html', content=content, filename=filename)
    elif filename == 'helloworld':
        content = {
            'title2': file_content2.get('title'),
            'created_time2': file_content2.get('created_time'),
            'content2': file_content2.get('content'),
        }
        return render_template('file.html', content=content, filename=filename)

    else:
        abort(404)

    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, port=3000)
