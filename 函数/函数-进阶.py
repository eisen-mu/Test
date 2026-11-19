""""""
"""
函数-变量的作用域
指变量的作用范围，标识这个变量在哪里可以使用，在哪里不可以使用
分为两类：
全局变量：在函数外定义的变量，整个文件（包括函数中）都可以使用，通常定义在顶部
局部变量：在函数内定义的变量，只能在函数内使用，外部无法访问，函数执行完后会销毁内部的局部变量

global关键字：用于明确告诉Python解释器，在函数中要使用的是全局变量而不是局部变量，可以在函数内部修改全局变量的值
声明使用全局变量必须在用过这个变量之前，不能先用了局部变量再说要用全局变量

尽量避免在函数中使用全局变量，会使代码难以维护和调试
考虑使用函数参数和返回值来传递数据，而不是依赖全局变量
global主要用在程序的状态、配置和计数器等场景中

传参方式：指调用函数的时候，传递实参的方式
1. 位置参数：调用函数时，根据函数定义时的位置来传递参数
要求；调用与定义时参数顺序完全一致
2. 关键字参数：调用参数时以函数定义时的形参名称为关键字，以“键-值”对的方式来传递参数
形参名 = 值
这种方式不要求顺序
位置参数和关键字参数可以混用，但必须是位置参数在前，关键字在后

默认参数：也成缺省参数，定义参数时为参数提供默认值，调用函数时，可以不传递有默认值的函数
定义函数时，让 指定形参 = 值 即可
默认参数必须放在没有默认值的参数之后

不定长参数：也叫可变参数，用于函数定义时参数个数不确定的场景
可以通过位置参数传递，也可以通过关键字参数传递

不定长参数-位置传递：（*args）
将多个参数封装到一个元组中传递 
约定俗成写成*args ，arguments即参数

不定长参数-关键字传递“（**kwargs）
key arguments，关键字参数
将多个参数和关键字封装成一个字典

参数类型：
1. 普通参数-可以是数字、布尔、字符串、列表、元组、集合、字典等
2. 特殊参数：函数，相当于函数嵌套

匿名函数：
没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写
（常规def的函数叫命名函数，因为有函数名）
# 定义匿名函数
lambda 参数列表：函数体
例如
add = lambda x,y : x+y
用于简单函数的定义，自动返回函数结果，通常作为高阶函数的参数使用
将lambda表达式赋值给一个变量，通过变量调用函数

# 递归调用：函数中自己调用自己的情况
一定要指定终结点，否则无限递归
在函数中用if语句给定终止条件，以及对应的返回值

# 类型注解：Python中的一种语法特性，用于明确标识变量、函数参数和返回值的数据类型，从而使代码更清晰、安全，易维护
多种类型可以用|分隔开
类型推断：Python解释器自动推断出变量、表达式或函数返回值的数据类型的能力，无需开发者显式声明

# 函数的类型注解：
为函数添加类型注解，主要是为函数参数和返回值添加类型注解

def calc(score: list[int]) -> float
这里形参定义为list，里面每一个都是整数，返回值为浮点数


为了写的更清楚，但python仍然是动态类型

定义变量
a: int = 123
score: float = 3.14
hobby: str = "Python"
flag: bool = True
pic: None = None

name: list[str] = ['A', 'B', 'C']] ---->指这个list中的每一个元素都是字符串
phones：set(str) = {'23443234', '124231452')
options: dict[str, int] = {'count': 0, 'total': 0}
goods: tuple[str, int, int] = ('手机', 5999, 1)

"""
# num = 100
#
# # 定义函数
# def circle_area(r):
#     # 布局变量: 只能在函数内部使用
#     global num
#     num = 10000
#     pi = 3.14
#     area = pi * r * r
#     print("num = ", num) # 10000
#
#     return area
#
# # 调用函数
# c_area = circle_area(10)
# print(c_area)
#
# print("num = ", num) # 10000

# # 定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}


# # 传参方式一: 位置参数
# stu = reg_stu("张三", 18, "男", "北京")
# print(stu)
#
# # 传参方式二: 关键字参数
# stu = reg_stu(name="王林", age=28, gender="男", city="北京")
# print(stu)
#
# stu = reg_stu(age=20, gender="女", city="北京", name="李慕婉")
# print(stu)
#
# # 传参方式三: 位置参数 + 关键字参数 ---> 位置参数在前, 关键字参数在后
# stu = reg_stu("李慕婉", 20, gender="女", city="北京")
# print(stu)


# ----------------------------------------- 函数 - 默认参数 -----------------------------------------
# 定义函数
# def reg_stu(name, age, gender="男", city="北京"):
#     print(f"注册成功, 姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city}
#
# # 调用函数
# stu = reg_stu("王林", 20)
# print(stu)
#
# stu = reg_stu("李慕婉", 18, "女")
# print(stu)
#
# stu = reg_stu("韩立", 22, city="上海")
# print(stu)

# print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222))


# ----------------------------------------- 函数 - 不定长参数(位置参数 *args --> 元组) -----------------------------------------
# 需求: 根据传入的这批数据, 计算这批数据的最小值, 最大值, 平均值
# def calc_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#     return min_data, max_data, round(avg_data, 1)
#
# # 调用函数
# print(calc_data(2, 7, 9, 10, 45))
#
# print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222))

# 函数 - 不定长参数(关键字参数 **kwargs --> 字典) ----------------------------------
# 需求: 根据传入的这批数据, 计算这批数据的最小值, 最大值, 平均值
# def calc_data(*args, **kwargs):
#     """
#     根据传入的这批数据, 计算这批数据的最小值, 最大值, 平均值
#     :param args: 不定长位置参数, 需要计算的这批数据
#     :param kwargs: 不定长关键字参数
#          round: 保留的小数位个数
#          print: 是否打印输出
#     :return: 最小值, 最大值, 平均值
#     """
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)
#
#     if kwargs.get("round") is not None:
#         # 甚至可以写is
#         avg_data = round(avg_data, kwargs.get("round"))
#
#     if kwargs.get("print"):
#         print(f"计算出来的最小值: {min_data}, 最大值: {max_data}, 平均值:{avg_data}")
#
#     return min_data, max_data, avg_data
#
# # 调用函数
# print(calc_data(2, 7, 9, 10, 45, round=3, print=True))
#
# print(calc_data(2, 7, 9, 10, 45, 73, 37, 93, 92, 111, 222, round=4, print=False))

# 需求3: 完成如下列表的排序操作, 按照每一个元素的字符个数, 从小到大排序 ;
# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
# print(data_list)
#
# data_list.sort(key=lambda item : len(item)) # 匿名函数典型的应用场景 .
# # 这里也可以直接写key=len，因为len是已经存在的函数
# print(data_list)

'定义一个函数，根据传入的数字计算该数字的阶乘'

# def jiecheng(n):
#     """
#     计算n的阶乘
#     :param n: 要计算的数
#     :return: n的阶乘
#     """
#     # 给定终止条件
#     if n == 1:
#         return 1
#     else:
#         return n * jiecheng(n-1)
# a = jiecheng(5)
# print(a)
"""
定义一个函数，用于传入一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
规则如下：
优惠券需要商品金额满5000才能使用，且优惠券金额不能超过商品总价
积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元，且抵扣金额不能超过商品总价，积分只能整百抵扣
"""
# def order_cost(*args:tuple[str,int,int], coupon = 0, score = 0, express = 0):
#     # 定义函数时规定缺省值
#     """
#     根据传入的商品信息、优惠、积分和运费信息计算订单总金额
#     :param args: 商品信息（商品名，价格，数量） --->如（"鼠标",188,2)("键盘，388,1）
#     :param coupon:优惠券
#     :param score:积分
#     :param express:运费
#     :return:订单总金额
#     """
#     # 订单总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
#     # 1. 计算商品总金额
#     price_list = [goods[1] * goods[2] for goods in args]
#     total_cost = sum(price_list)
#     # 2. 扣减优惠券
#     if total_cost >= coupon and total_cost >= 5000:
#          total_cost -= coupon
#
#     # 3. 扣减积分折扣
#     if total_cost >= score // 100 and total_cost >= 5000:
#         total_cost -= coupon
#
#     # 4. 增加运费
#     total_cost += express
#     return total_cost
#
# #测试
# total = order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1), coupon =10, score = 4000, express = 9.9)
# print(total)

# 变量定义 - 未指定类型注解 ---> 类型推断
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E", 100]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count":2 , "total":10}
goods = ("手机", 6999, 1)

names.append("X")
names.append(10010)
names.append(10010.0)

print(names)
