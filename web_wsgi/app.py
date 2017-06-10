#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>HUU</h1>'

@app.route('/signin',methods=['GET'])
def singin():
    return '''    <form action="/singin" method="post">
    <label for="username" value="username">username</label>
    <input type="text" name="username">
    <br>
    <label for="password" value="password">password</label>
    <input type="text" name="password">
    <br>
    <input type='submit' value="登录">
    </form>'''

@app.route('/singin',methods=['POST'])
def login():
    if request.form['username']=='huu' and request.form['password']=='hubang1994':
        return '<h1>Success</h1>'
    else:
        return '<h1>Failed</h1>'
if __name__ == '__main__':
    app.run()

