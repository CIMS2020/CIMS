import cgi, cgitb

# 创建FieldStorage的实例化
form = cgi.FieldStorage()
# 获取html页面传递过来的数据值
user_name = form.getvalue('user_name')
user_age = form.getvalue('user_age')
user_id = form.getvalue('user_id')
user_tel = form.getvalue('user_tel')
user_money = form.getvalue('user_money')
print('user_name:',user_name)
print('user_age:',user_age)
print('user_id:',user_id)
print('user_tel:',user_tel)
print('user_money:',user_money)