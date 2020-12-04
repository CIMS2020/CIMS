from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import webbrowser

from sqlalchemy.sql import func
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:asd@test'#(替换成自己的用户名，密码和dsn）
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
