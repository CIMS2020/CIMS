import webbrowser
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_bootstrap import forms
from wtforms import ValidationError
import time
import json
from datetime import datetime , date , timedelta
from flask import render_template,request,redirect,url_for,flash,session,jsonify,send_from_directory
import requests
import base64


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:asd@test'#(替换成自己的用户名，密码和dsn）
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class testflask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    canname = db.Column(db.String(30))

class restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rname = db.Column(db.String(30))
    canno = db.Column(db.Integer)
    cost = db.Column(db.FLOAT)

class ingeredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inname = db.Column(db.String(30))
    price = db.Column(db.FLOAT)
    amount = db.Column(db.Integer)
    data = db.Column(db.String(30))
    canno = db.Column(db.String(30))
    Class = db.Column(db.String(30))

class food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    price = db.Column(db.FLOAT)
    rno = db.Column(db.String(30))

class worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wno = db.Column(db.String(30))
    wsex = db.Column(db.String(30))
    sale = db.Column(db.FLOAT)
    wduring = db.Column(db.String(30))
    rno = db.Column(db.String(30))

class stu(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30))
    ssex = db.Column(db.String(30))
    tel = db.Column(db.String(30))
    dept = db.Column(db.String(30))

class cost(db.Model):
    sno = db.Column(db.String(30), primary_key=True)
    date = db.Column(db.String(30))
    cost = db.Column(db.FLOAT)
    rno = db.Column(db.String(30))

class card(db.Model):
    sno = db.Column(db.String(30), primary_key=True)
    money = db.Column(db.FLOAT)
    tel = db.Column(db.String(30))

class adm(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    ano = db.Column(db.String(30))

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
#add



@app.route('/register', methods=["get", "post"])
def register():
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        userid= request.form.get("userid")
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            print("参数不足")
            # flash("参数不足")
        elif password != password2:
            print("两次密码不一致")
            #flash("两次密码不一致")
        else:
            # 假装做注册操作
            # flash("注册成功！")

            print("注册成功！")

            print(userid,username, password, password2)
        # print(userid,username, password, password2)

    return render_template('register.html')


@app.route('/canteen')
def canteen():
    """Renders the canteen page."""
    return render_template(
        'canteen.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/comsumers')
def comsumers():
    """Renders the comsumers page."""
    return render_template(
        'comsumers.html',
        title='Comsumers',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/login', methods=["get", "post"])
def login():
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        userid= request.form.get("userid")
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            print("参数不足")
            # flash("参数不足")
        elif password != password2:
            print("两次密码不一致")
            # flash("两次密码不一致")
        else:
            # 假装做注册操作
            #flash("注册成功！")
            print("注册成功！")
            print(userid,username, password, password2)
    return render_template('login.html')
    #10*2 选择题
#名词解释 3*4题
#简答 7 30分
#分析设计4 38分
#过程模型  uml图
#数据字典
#软件测试策略
#软件体系结构
#基本路径测试
#评审技术
#挣值分析
#风险管理
@app.route('/shop')
def shop():
    """Renders the shop page."""
    return render_template(
        'shop.html',
        title='Shop',
        year=datetime.now().year,
        message='Your application description page.'
    )





if __name__ == '__main__':
    db.create_all()
    url = "http://127.0.0.1:5000"
    webbrowser.open_new(url)
    app.run()
