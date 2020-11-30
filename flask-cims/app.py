import webbrowser
from datetime import datetime

from flask import Flask, render_template

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

@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Your application description page.'
    )
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
