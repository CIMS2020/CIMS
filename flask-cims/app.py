import webbrowser
from datetime import datetime
from flask import flash
from flask import Flask, render_template, request
from flask_bootstrap import forms
from wtforms import ValidationError
import time
import json
from datetime import datetime , date , timedelta
from flask import render_template,request,redirect,url_for,flash,session,jsonify,send_from_directory
from flask import Flask,url_for,render_template,request,make_response,session,flash,get_flashed_messages
import  forms
import requests
import base64


app = Flask(__name__)


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
        test=""
        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            print("参数不足")
            return render_template('register.html',text="失败")
        elif password != password2:
            print("两次密码不一致")
            return render_template('register.html',text="失败")
        else:
            # 假装做注册操作
            print(userid,username, password, password2)
            return render_template('register.html', text="成功")

    return render_template('register.html')


@app.route('/canteen')
def canteen():
    """Renders the canteen page."""
    return render_template(
        'canteen.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
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

app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'

@app.route('/login', methods=["get", "post"])
def login():
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        userid= request.form.get("userid")
        password = request.form.get("password")
        flash('666')
        if not all([userid, password]):
            # 向前端界面弹出一条提示(闪现消息)
            return render_template(
                'login.html',
                title='Shop',
                year=datetime.now().year,
                message='信息不全'
            )
        else:
            # 假装做注册操作
            print(userid, password)

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
    url = "http://127.0.0.1:5000"
    webbrowser.open_new(url)
    app.run()
