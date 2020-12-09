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
from flask import Flask, render_template, request, flash, make_response
from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired, EqualTo





app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:asd@test'#(替换成自己的用户名，密码和dsn）
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# 开启session
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'
# app.config["SECRET_KEY"] = "abcd"
app.config["WTF_CSRF_ENABLED"] = False


# 数据库数据类型
class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shopname = db.Column(db.String(30))
    shopno = db.Column(db.String(30))
    shopaddr = db.Column(db.String(30))

class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goodsname = db.Column(db.String(30))
    amount = db.Column(db.Integer)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    price = db.Column(db.String(30))
    shopno = db.Column(db.String(30))

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wno = db.Column(db.String(30))
    #wsex = db.Column(db.String(30))
    sal = db.Column(db.String(30))
    shopno = db.Column(db.String(30))
    wname = db.Column(db.String(30))
    wtel = db.Column(db.String(30))
class stu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(30))
    sname = db.Column(db.String(30))
    sage = db.Column(db.String(30))
    tel = db.Column(db.String(30))

class Cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(30))
    date = db.Column(db.String(30))
    cost = db.Column(db.String(30))
    shopno = db.Column(db.String(30))

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    sno = db.Column(db.String(30))
    money = db.Column(db.String(30))
 #   tel = db.Column(db.String(30))

class Adm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #ano = db.Column(db.String(30))
    aname = db.Column(db.String(30))
    password = db.Column(db.String(30))



# 表单数据类型
def PasswordChcek():
    def check(form, field):
        user = Adm.query.filter_by(aname=form.username.data).first()
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
    submit = SubmitField(label="查询")

class AddWorker(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    workername = StringField(label="员工姓名", validators=[DataRequired("请输入员工姓名")])
    workerid = StringField(label="员工ID", validators=[DataRequired("请输入员工ID")])
    workertel = StringField(label="员工电话", validators=[DataRequired("请输入员工电话")])
    workersal = StringField(label="员工工资", validators=[DataRequired("请输入员工工资")])
    submit2 = SubmitField(label="添加")

class SearchWorker(FlaskForm):
    workerid = StringField(label="员工ID", validators=[DataRequired("请输入员工ID")])
    submit3 = SubmitField(label="查询")

class DeleteWorker(FlaskForm):
    shopid4 = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    workerid4 = StringField(label="员工ID", validators=[DataRequired("请输入员工ID")])
    submit4 = SubmitField(label="删除")

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
    submit = SubmitField(label="查询")

class SearchAllShops(FlaskForm):
    submit = SubmitField(label="查询")

class SearchList(FlaskForm):
    shopid = StringField(label="店铺ID", validators=[DataRequired("请输入店铺ID")])
    submit = SubmitField(label="查询菜单")

class Consuming(FlaskForm):
    userid = StringField(label="UID", validators=[DataRequired("请输入UID")])
    foodid = StringField(label="食物序号", validators=[DataRequired("请输入食物序号")])
    date = StringField(label="日期", validators=[DataRequired("请输入日期")])
    #shopid = StringField(label="", validators=[DataRequired("请输入日期")])
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


#add



@app.route('/register', methods=["get", "post"])
def register():
    form = Register()
    if form.validate_on_submit():
        admin = Adm(aname=form.username.data, password=form.password.data)
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

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    price = db.Column(db.FLOAT)
    shopno = db.Column(db.String(30))
'''
# @app.route('/canteen', methods=["get", "post"])
@app.route('/create_consumer', methods=["get", "post"])
def create_consumer():
    form1 = CreateCon()
    myData = stu.query.all()
    if form1.validate_on_submit():
        userid = form1.userid.data
        card = Card(sno=userid,money='0')
        db.session.add(card)
        db.session.commit()
        student = stu(sname=form1.username.data,sage=form1.age.data,sno=form1.userid.data,tel=form1.tel.data)
        db.session.add(student)
        db.session.commit()

        flash("创建消费者成功！")
        return redirect(url_for('create_consumer'))
    """Renders the canteen page."""
    return render_template(
        'create_consumer.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
        form1=form1,
        stu = myData
    )
@app.route('/create_shop', methods=["get", "post"])
def create_shop():
    form3 = CreateShop()
    form4 = SearchAllShops()
    myData = Shop.query.all()
    print('Shop:', myData)

    if form3.validate_on_submit():
        shop = Shop(shopname=form3.shopname.data,shopno=form3.shopid.data,shopaddr=form3.shopaddr.data)
        db.session.add(shop)
        db.session.commit()
        flash("创建店铺成功!")
        return redirect(url_for('create_shop'))

    return render_template(
        'create_shop.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
        form3=form3,
        form4=form4,
        shop=myData
    )

@app.route('/ware_manage', methods=["get", "post"])
def ware_manage():
    form5 = AddGoods()
    form6 = SearchWare()
    myData = Goods.query.all()
    if form5.validate_on_submit():
        goods = Goods(goodsname=form5.goodsname.data,amount=form5.goodsnum.data)
        db.session.add(goods)
        db.session.commit()
        flash("添加食材成功！")
        return redirect(url_for('ware_manage'))
    return render_template(
        'ware_manage.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
        form5=form5,
        form6=form6,
        Goods=myData
    )


'''
class Invest(FlaskForm):
    userid = StringField(label="UID", validators=[DataRequired("请输入UID")])
    recharge_amount = StringField(label="金额", validators=[DataRequired("请输入金额")])
    submit = SubmitField(label="充值")
class Cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(30))
    date = db.Column(db.String(30))
    cost = db.Column(db.FLOAT)
    rno = db.Column(db.String(30))
class Card(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    sno = db.Column(db.String(30))
    money = db.Column(db.FLOAT)
 #   tel = db.Column(db.String(30))
 
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    price = db.Column(db.FLOAT)
    shopno = db.Column(db.String(30))
'''
@app.route('/invest',methods=["get", "post"])
def invest():
    form1 = Invest()
    form2 = SearchConsume()
    if form1.validate_on_submit():
        add_money = form1.recharge_amount.data
        card = Card.query.filter(Card.sno ==form1.userid.data).first()
        now_money = int(card.money)
        now_money +=int(add_money)
        card.money =str(now_money)
        db.session.commit()
        flash("充值成功！")
        return render_template(
            'Invest.html',
            title='Comsumers',
            year=datetime.now().year,
            message='Your application description page.',
            form1=form1,
            form2=form2,
        )
    if form2.validate_on_submit():
        userid = form2.userid.data
        nowmoney = Card.query.filter(Card.sno==userid).first()
        nowmoney = nowmoney.money
        return render_template(
            'Invest.html',
            title='Comsumers',
            year=datetime.now().year,
            message='Your application description page.',
            rest=nowmoney,
            form1=form1,
            form2=form2,
        )
    """Renders the comsumers page."""
    return render_template(
        'Invest.html',
        title='Comsumers',
        year=datetime.now().year,
        message='Your application description page.',
        form1=form1,
        form2=form2,
    )
'''class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    price = db.Column(db.String(30))
    shopno = db.Column(db.String(30))
    
class Cost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sno = db.Column(db.String(30))
    date = db.Column(db.String(30))
    cost = db.Column(db.String(30))
    shopno = db.Column(db.String(30))'''
@app.route('/mock_consume',methods=["get", "post"])
def mock_consume():
    form2 = SearchList()
    form3 = Consuming()
    myData = Shop.query.all()
    if form2.validate_on_submit():
        shopid = form2.shopid.data
        list = Food.query.filter(Food.shopno==shopid)
        return render_template(
            'mock_consume.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            form4=form2,
            form5=form3,
            shop=myData,
            list=list
        )
    if form3.validate_on_submit():
        userid=form3.userid.data
        foodid=form3.foodid.data
        date=form3.date.data
        ans =Food.query.filter(Food.id==foodid).first()
        price = ans.price
        shopid = ans.shopno
        cost = Cost(sno=userid,date=date,cost=price,shopno=shopid)
        db.session.add(cost)
        db.session.commit()
        flash("消费成功！")
        return render_template(
            'mock_consume.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            form4=form2,
            form5=form3,
            shop=myData,
            price=price
        )
    return render_template(
        'mock_consume.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
        form4=form2,
        form5=form3,
        shop=myData
    )






@app.route('/search_sales',methods=["get", "post"])
def search_sales():
    form1 = DailySearch()
    if form1.validate_on_submit():
        shopid = form1.shopid.data
        date = form1.date.data
        ans = Cost.query.filter( Cost.shopno==shopid).all()
        return render_template(
            'search_sales.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            form1=form1,
            ans=ans
        )
    return render_template(
        'search_sales.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
        form1=form1,
    )


'''class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wno = db.Column(db.String(30))
    wsex = db.Column(db.String(30))
    sale = db.Column(db.FLOAT)
    shopno = db.Column(db.String(30))'''
@app.route('/worker_manage',methods=["get", "post"])
def worker_manage():
    form2 = AddWorker()
    form3 = SearchWorker()
    form4 = DeleteWorker()
    form2.workerid.data='50'
    if form2.validate_on_submit():
        shopid = form2.shopid.data
        workername = form2.workername.data
        workid = form2.workerid.data
        workertel = form2.workertel.data
        workersal = form2.workersal.data
        worker = Worker(wno=workid,sal=workersal,shopno=shopid,wname=workername,wtel=workertel)
        # print(shopid,workername,workertel,workersal)
        db.session.add(worker)
        db.session.commit()
        flash("添加员工成功！")
        return render_template(
            'worker_manage.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            form2=form2,
            form3=form3,
            form4=form4,
        )
    if form3.validate_on_submit():
        workid = form3.workerid.data
        ans = Worker.query.filter(Worker.wno==workid).first()
        # print(ans.wno)
        flash("查询员工成功！")
        return render_template(
            'worker_manage.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            form2=form2,
            form3=form3,
            form4=form4,
            ans=ans,
        )
    if form4.validate_on_submit():
        shopid = form4.shopid4.data
        worker = form4.workerid4.data
        tem = Worker.query.filter(Worker.wno==worker).first()
        db.session.delete(tem)
        db.session.commit()
        flash("删除员工成功！")
        return render_template(
            'worker_manage.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            form2=form2,
            form3=form3,
            form4=form4,
        )


    return render_template(
        'worker_manage.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
        form2=form2,
        form3=form3,
        form4=form4,
    )




@app.route('/main_task', methods=["get", "post"])
def main_task():
    myData = Goods.query.all()
    form1 = GetStuff()
    form2 = AddtoList()
    form3 = SearchList()
    if form1.validate_on_submit():
        shopid = form1.shopid.data
        goodsname = form1.goodsname.data
        goodsnum = form1.goodsnum.data
        ware = Goods.query.filter(Goods.goodsname==goodsname).first()
        ware.amount -= int(goodsnum)
        db.session.commit()
        flash("取出成功！")
        return render_template(
            'main_task.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            ans=myData,
            form7=form1,
            form8=form2,
            form9=form3
        )
    if form2.validate_on_submit():
        shopid = form2.shopid.data
        foodname = form2.foodname.data
        price = form2.price.data
        food = Food(fname=foodname,price=price,shopno=shopid)
        db.session.add(food)
        db.session.commit()
        flash("添加成功！")
        return render_template(
            'main_task.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            ans=myData,
            form7=form1,
            form8=form2,
            form9=form3
        )
    if form3.validate_on_submit():
        shopid = form3.shopid.data
        #list = Food.query.all()
        list = Food.query.filter(Food.shopno == shopid)
        return render_template(
            'main_task.html',
            title='Canteen',
            year=datetime.now().year,
            message='Your application description page.',
            ans=myData,
            form7=form1,
            form8=form2,
            form9=form3,
            list = list,
        )

    return render_template(
        'main_task.html',
        title='Canteen',
        year=datetime.now().year,
        message='Your application description page.',
        ans = myData,
        form7=form1,
        form8=form2,
        form9=form3
    )



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
    user = Adm.query.filter_by(aname=aname).first()
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
    # db.drop_all()
    # db.create_all()
    url = "http://127.0.0.1:5000"
    webbrowser.open_new(url)
    app.run(debug=True)
