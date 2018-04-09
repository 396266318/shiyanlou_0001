# -*- coding: UTF-8 -*-

from flask import request
from flask import Flask
from flask import render_template
from ele import ele_red_packet


app = Flask(__name__)


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def phone_number_form():
    phone_number = request.form['phone']
    get_red_packet = ele_red_packet(phone_number)
    # print(get_red_packet)
    return render_template('index.html', phone_number=get_red_packet)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)