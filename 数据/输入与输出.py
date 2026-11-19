"""input语句（函数）是python内置的功能，获取键盘输入
具体用法s = input（提示信息）
所有input函数获取的键盘录入数据的格式均为字符串，即使是数字
name = input("请输入你的姓名")
print(f"欢迎{name}")
age = input("请输入你的年龄")
print(f"你今年{age}岁")
"""

# 模拟银行卡取款
acc = 10000 #余额
#输入密码
password = input("请输入密码")
print(f"正确,{password}")
#输入取款金额
num = input("请输入取款金额")
#计算余额并输出，num转为int
print(f"余额为：{acc - int(num)}")