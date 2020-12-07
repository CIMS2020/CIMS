import webbrowser
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import flash
from flask import Flask, render_template, request
from flask_bootstrap import forms, Bootstrap
from flask_bootstrap import Bootstrap   #导入
from wtforms import ValidationError
import time
import json
from datetime import datetime , date , timedelta
from flask import render_template,request,redirect,url_for,flash,session,jsonify,send_from_directory
from flask import Flask,url_for,render_template,request,make_response,session,flash,get_flashed_messages
import requests
import base64
from wtforms.validators import DataRequired, EqualTo
from wtforms.fields import *
from flask_wtf import FlaskForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:asd@test'#(替换成自己的用户名，密码和dsn）
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# 开启session
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'
# app.config["SECRET_KEY"] = "abcd"
app.config["WTF_CSRF_ENABLED"] = False




from flask import Flask, render_template, request, flash, make_response
from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired, EqualTo



# 数据库数据类型
class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shopname = db.Column(db.String(30))
    shopno = db.Column(db.Integer)
    shopaddr = db.Column(db.String(30))

class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goodsname = db.Column(db.String(30))
    amount = db.Column(db.Integer)

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
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(30))
    sname = db.Column(db.String(30))
    sage = db.Column(db.Integer)
    tel = db.Column(db.String(30))


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
    id = db.Column(db.Integer, primary_key=True)
    #ano = db.Column(db.String(30))
    aname = db.Column(db.String(30))
    password = db.Column(db.String(30))



# 表单数据类型
def PasswordChcek():
    def check(form, field):
        user = adm.query.filter_by(aname=form.username.data).first()
        if user is None :
            raise ValidationError('')
        if field.data != user.password :
            raise ValidationError('密码错误')
    return check
class Login(FlaskForm):
    username = StringField(label="用户名", validators=[DataRequired("请输入用户名")])
    password = PasswordField(label="密码", validators=[DataRequired("请输入密码"),PasswordChcek()])
    submit = SubmitField(label="登录")

class Register(FlaskForm):
    username = StringField(label="用户名", validators=[DataRequired("请输入用户名")])
    password = PasswordField(label="密码", validators=[DataRequired("请输入密码")])
    password2= PasswordField(label="确认密码", validators=[DataRequired("请输入密码"), EqualTo('password', "密码输入不一致")])
    submit = SubmitField(label="注册")

class CreateCon(FlaskForm):
    username = StringField(label="用户名", validators=[DataRequired("请输入用户名")])
    userid = StringField(label="UID", validators=[DataRequired("请输入UID")])
    age = StringField(label="年龄", validators=[DataRequired("请输入年龄")])
    tel = StringField(label="手机号", validators=[DataRequired("请输入手机号")])
    submit = SubmitField(label="添加")

class CreateShop(FlaskForm):
    shopname = StringField(label="店铺名", validators=[DataRequired("请输入店铺名")])
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    shopaddr = StringField(label="店铺地址", validators=[DataRequired("请输入店铺地址")])
    submit = SubmitField(label="添加")

class AddGoods(FlaskForm):
    goodsname = StringField(label="货物名", validators=[DataRequired("请输入货物名")])
    goodsnum = StringField(label="货物数量", validators=[DataRequired("请输入货物数量")])
    submit = SubmitField(label="添加")

class SearchAllCon(FlaskForm):
    submit = SubmitField(label="查询")



class SearchWare(FlaskForm):
    submit = SubmitField(label="查询")

#Shop.html
class DailySearch(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    date = StringField(label="日期", validators=[DataRequired("请选择日期")])
    submit = SubmitField(label="添加")

class AddWorker(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    workername = StringField(label="员工姓名", validators=[DataRequired("请输入员工姓名")])
    workerid = StringField(label="员工ID", validators=[DataRequired("请输入员工ID")])
    workertel = StringField(label="员工电话", validators=[DataRequired("请输入员工电话")])
    workersal = StringField(label="员工工资", validators=[DataRequired("请输入员工工资")])
    submit = SubmitField(label="添加")

class SearchWorker(FlaskForm):
    workerid = StringField(label="员工ID", validators=[DataRequired("请输入员工ID")])
    submit = SubmitField(label="查询")

class DeleteWorker(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    workerid = StringField(label="员工ID", validators=[DataRequired("请输入员工ID")])
    submit = SubmitField(label="删除")

class UpdateWorker(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    workerid = StringField(label="员工ID", validators=[DataRequired("请输入员工ID")])
    workername = StringField(label="员工姓名", validators=[DataRequired("请输入员工姓名")])
    workertel = StringField(label="员工电话", validators=[DataRequired("请输入员工电话")])
    workersal = StringField(label="员工工资", validators=[DataRequired("请输入员工工资")])
    submit = SubmitField(label="添加")

class GetStuff(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    goodsname = StringField(label="货物名", validators=[DataRequired("请输入货物名")])
    goodsnum = StringField(label="货物数量", validators=[DataRequired("请输入货物数量")])
    submit = SubmitField(label="取出")

class AddtoList(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    foodname = StringField(label="食物名称", validators=[DataRequired("请输入食物名称")])
    price = StringField(label="食物价格", validators=[DataRequired("请输入食物价格")])
    submit = SubmitField(label="添加")

class BrowseList(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    submit = SubmitField(label="添加")

#Consumer.html
#充值
class Invest(FlaskForm):
    userid = StringField(label="UID", validators=[DataRequired("请输入UID")])
    recharge_amount = StringField(label="金额", validators=[DataRequired("请输入金额")])
    submit = SubmitField(label="充值")

class SearchConsume(FlaskForm):
    userid = StringField(label="UID", validators=[DataRequired("请输入UID")])
    submit = SubmitField(label="充值")

class SearchAllShops(FlaskForm):
    submit = SubmitField(label="查询")

class SearchList(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    submit = SubmitField(label="查询菜单")

class Consuming(FlaskForm):
    userid = StringField(label="UID", validators=[DataRequired("请输入UID")])
    foodid = StringField(label="食物序号", validators=[DataRequired("请输入食物序号")])
    date = StringField(label="日期", validators=[DataRequired("请输入日期")])
    submit = SubmitField(label="确定")


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
    form = Register()
    if form.validate_on_submit():
        admin = adm(aname=form.username.data, password=form.password.data)
        db.session.add(admin)
        db.session.commit()
        flash("注册成功！")
        return redirect(url_for('login'))

    return render_template('register.html',
                           title = 'Register',
                           form = form)
'''
class stu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(30))
    sname = db.Column(db.String(30))
    sage = db.Column(db.Integer)
    tel = db.Column(db.String(30))
    
    
class shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shopname = db.Column(db.String(30))
    shopno = db.Column(db.Integer)
    shopaddr = db.Column(db.FLOAT)
    
class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goodsname = db.Column(db.String(30))
    amount = db.Column(db.Integer)
'''
@app.route('/canteen')
def canteen():
    form1 = CreateCon()
    form2 = SearchAllCon()
    form3 = CreateShop()
    form4 = SearchAllShops()
    form5 = AddGoods()
    form6 = SearchWare()
    if form1.validate_on_submit():
        student = stu(sname=form1.username.data,sage=form1.age.data,sno=form1.userid,tel=form1.tel)
        db.session.add(student)
        db.session.commit()
        flash("创建消费者成功！")
    """Renders the canteen page."""
    if form2.validate_on_submit():
        myData = stu.query.all()
        output = []
        for record in myData:
            data = {}
            data['sno'] = record.sno
            data['sname'] = record.sname
            data['sage'] = record.sage
            data['tel'] = record.tel
            output.append(data)
        print(output)
        return jsonify({'message': output})
    if form3.validate_on_submit():
        shop = Shop(shopname=form3.shopname.data,shopno=form3.shopid,shopaddr=form3.shopaddr)
        db.session.add(shop)
        db.session.commit()
        flash("创建店铺成功!")
    if form4.validate_on_submit():
        myData = Shop.query.all()
        output = []
        for record in myData:
            data = {}
            data['shopname'] = record.shopname
            data['shopno'] = record.shopno
            data['shopaddr'] = record.shopaddr
            output.append(data)
        return jsonify({'message': output})
    if form5.validate_on_submit():
        goods = Goods(goodsname=form5.goodsname.data,amount=form5.goodsnum)
        db.session.add(goods)
        db.session.commit()
        flash("添加食材成功！")
    if form6.validate_on_submit():
        myData = Goods.query.all()
        output = []
        for record in myData:
            data = {}
            data['id'] = record.id
            data['goodsname'] = record.goodsname
            data['amount'] = record.amount
            output.append(data)
        print(output)
        return jsonify({'message': output})
    return render_template(
        'canteen.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
        form1=form1,
        form2=form2,
        form3=form3,
        form4=form4,
        form5=form5,
        form6=form6,
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


@app.route("/login", methods=["GET", "POST"])
def login():
     form = Login()
     if form.validate_on_submit():
         session['name'] = form.username.data
         session.permanent = True  # 是否保存用户登录状态
         flash("登录成功")
         return redirect(url_for('home'))
     return render_template('login.html',
                            title='Login',
                            form=form, )

@app.context_processor
def my_context_processor():
    aname = session.get('name')
    user = adm.query.filter_by(aname=aname).first()
    if user:
        return {'user': user}
    return{}

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
    db.drop_all()
    db.create_all()
    url = "http://127.0.0.1:5000"
    webbrowser.open_new(url)
    app.run(debug=True)
