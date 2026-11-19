""""""
"""
面向过程编程：把一个需求分解成一系列要执行的步骤，然后按照步骤一次执行这些任务，关注流程和步骤
适用于简单、线性的任务

对象：Python中万物皆对象
把一个人/物的特征（python中叫属性）和功能（python中叫方法）打包到一起，是面向对象编程的基本单元，关注谁来帮我做这件事

类：描述的是一组具有相同属性和方法的模板
对象：是类的实例，是基于类创建出来的
创建对象的过程也称为对象的实例化，一个类可以创建无数个对象

# 定义类：
class 类名：           class Car:
    pass                 pass   
# 创建对象
对象名 = 类名（）          c1 = Car()
对象名.属性名1 = 属性值1     c1.brand = 'BMW'
对象名.属性名2 = 属性值2     c1.name = 'x5'

！！！注意：类名的命名规范遵循大驼峰命名法，每个单词首字母都是大写，单词之间没有分隔符（包括空格）如UserInfo， UserAccount

对象的属性可以动态添加，但不推荐！！！

# class Car:
#     pass
# # 动态地为对象添加属性----不推荐
# c1 = Car()
# c1.brand = 'BMW'
# c1.name = 'x5'
# c1.price = 588888
# print(c1)
# print(c1.brand)
# print(c1.__dict__)
"这里的__dict__是用户自定义类实例的一个特殊属性，用于以字典形式存储对象的属性"


类的标准定义：

class 类名：
    def __init__(self,参数列表）
    self.属性名 = 参数值
    self.属性名 = 参数值
    
创建对象

对象名 = 类名（参数1，参数2，……）

"""
# 定义类
# class Car:
#     def __init__(self,c_brand,c_name,c_price):
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
# # 创建对象
# c1 = Car('BMW','x5',888888)
# print(c1.__dict__)
# print(c1)

"""
实例方法
在类中定义实例方法时，定义语法与之前学习的函数定义方法一致
# 定义类
class 类名：
    def __init__(self,参数列表）
    self.属性名 = 参数值
    self.属性名 = 参数值
    
    def 方法名（self, 形参列表）
    ...
    def 方法名（self, 形参列表）
    ...

# 创建对象:
对象名 = 类名（参数列表）
对象名.方法名（实参）

"""
# 定义类
# class Car:
#     def __init__(self,c_brand,c_name,c_price):
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#     def running(self):
#         print(f" {self.brand},{self.name}正在行驶")
#     def total_cost(self,discount,rate):
#         """
#         计算提车总费用，两个部分，车的价格和税费
#         :param discount: 折扣
#         :param rate: 税率
#         :return: 提车总费用
#         """
#         return self.price * discount + self.price * rate

# # 创建对象
# c1 = Car('BMW','x5',888888)
# # 调用对象中的方法
# total_cost = c1.total_cost(discount=0.8,rate=0.1)
# print(f"提车总价为：{total_cost:.0f}")
# c1.running()

"""
魔法方法：
指python中提供的以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如__init__
魔法方法不需要手动调用，python在合适的时候自动调用
常见的：
__init__:初始化方法
__str__:字符串表示的方法
__eq__:比较两个对象是否相等（equal）
__lt__,__gt__,__le__,__ge__:比较两个对象大小，小于less than，小于等于less than or equal，大于 greater than
__dict__:

"""
# class Car:
#     def __init__(self,c_brand,c_name,c_price):
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#     "输出对象的时候会自动调用，将对象转化为字符串"
#     def __str__(self):
#         return f"{self.brand} {self.name} {self.price}"
#
#     def __eq__(self,other):
#         return self.brand == other.brand and self.name == other.name and self.price == other.price
#     def __lt__(self,other):
#         return self.price < other.price
#
# # 创建对象
# c1 = Car('BMW','x5',888888)
# c2 = Car('BMW','x5',888888)
#
# print(c1 == c2)
# print(c1 < c2)
# print(c1 > c2)

"""
属性：分为实例属性和类属性
实例属性：属于每个具体对象的属性，每个对象都是独立的，各个对象特有的数据
通过实例对象名.属性名来操作
类属性：属于类本身的属性，所有实例共享，所有对象共享的数据或配置
通过类名.属性名来操作

通过实例查找属性时，会先查找实例属性，当实例属性不存在时，再查找类属性

"""
class Car:
    wheel = 4
    tax_rate = 0.1
    "上面两个都是类属性,所有实例对象共享，下面的都是实例属性"
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
c1 = Car("白色","Tesla","汉","180000")
print(c1.brand)
print(c1.wheel)
print(Car.wheel)
print(Car.tax_rate)

c2 = Car("黑色", "Tesla","model_Y","260000")
