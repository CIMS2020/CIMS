from flask import Flask, render_template, request, flash, make_response
from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
# 开启session
app.secret_key = "aasdfsdf"
# app.config["SECRET_KEY"] = "abcd"
app.config["WTF_CSRF_ENABLED"] = False


@app.route('/')
def hello_world():
    return 'Hello World!'


class Login(FlaskForm):
     username = StringField(label="用户名", validators=[DataRequired("请输入用户名")])
     password = PasswordField(label="密码", validators=[DataRequired("请输入密码")])
     password2 = PasswordField(label="密码", validators=[DataRequired("请输入密码"), EqualTo('password', "密码输入不一致")])
     submit = SubmitField(label="提交")


@app.route("/login", methods=["GET", "POST"])
def login():
     login_form = Login()
     if request.method == 'POST':
         if login_form.validate_on_submit():
             username = request.form.get("username")
             password = request.form.get("password")
             password2 = request.form.get("password2")
             print(username, password, password2)
             # return make_response("success")
             return "success"
         else:
             print("error")
             flash("参数错误请重新输入")
             # return render_template("demo004.html", form=login_form)

     # else:
     #     print("get")
     #     return render_template("demo004.html", form=login_form)
     return render_template("demo004.html", form=login_form)


 # 定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/demo2', methods=["get", "post"])
def demo2():
     register_form = Login()
     # 验证表单
     if register_form.validate_on_submit():
         # 如果代码能走到这个地方，那么就代码表单中所有的数据都能验证成功
         username = request.form.get("username")
         password = request.form.get("password")
         password2 = request.form.get("password2")
         # 假装做注册操作
         print(username, password, password2)
         return "success"
     else:
         if request.method == "POST":
             flash("参数有误或者不完整")

     return render_template('demo004.html', form=register_form)


if __name__ == '__main__':
     app.run(debug=True)