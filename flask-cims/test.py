from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import webbrowser

from sqlalchemy.sql import func
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:asd@test'#(替换成自己的用户名，密码和dsn）

db = SQLAlchemy(app)
class testflask(db.Model):  #创建model，对应数据库中的表
    PersonID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    LastName = db.Column(db.String(255))
    FirstName = db.Column(db.String(255))
    Address = db.Column(db.String(255))
    City = db.Column(db.String(255))

@app.route('/')
@app.route('/get_data', methods=['GET'])
def get_data():
    myData = testflask.query.all()
    output = []
    for record in myData:
        r_data = {}
        r_data['PersonID'] = record.PersonID
        r_data['FirstName'] = record.FirstName
        r_data['LastName'] = record.LastName
        r_data['Address'] = record.Address
        r_data['City'] = record.City
        output.append(r_data)
    return jsonify({'message': output})
@app.route('/add_data')
def add_data():
    exa = testflask(LastName='s',FirstName='wb',Address='fzu',City='fuzhou')
    db.session.add(exa)
    db.session.commit()
    myData = testflask.query.all()
    output = []
    for record in myData:
        r_data = {}
        r_data['PersonID'] = record.PersonID
        r_data['FirstName'] = record.FirstName
        r_data['LastName'] = record.LastName
        r_data['Address'] = record.Address
        r_data['City'] = record.City
        output.append(r_data)
    return jsonify({'message': output})
@app.route('/delete_data')
def delete_data():
    b = testflask.query.get(1)
    db.session.delete(b)
    db.session.commit()
    myData = testflask.query.all()
    output = []
    for record in myData:
        r_data = {}
        r_data['PersonID'] = record.PersonID
        r_data['FirstName'] = record.FirstName
        r_data['LastName'] = record.LastName
        r_data['Address'] = record.Address
        r_data['City'] = record.City
        output.append(r_data)
    return jsonify({'message': output})
if __name__ == '__main__':
    # db.create_all()
    url = "http://127.0.0.1:5000"
    webbrowser.open_new(url)
    app.run(debug=True)