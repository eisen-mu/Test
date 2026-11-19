"""变量：用来存储单个数据的容器
定义格式： 变量名 = 数值，将数值赋给变量
python允许动态类型，一个变量可以接收不同类型，但做项目一般一个变量还是用一个类型
type(要查看类型的数据)
isinstance(数据，类型），判定数据的类型是否是指定类型，返回布尔值
"""
A = 3.34
A = A+1
print(A)

A = True
print(A)
A = A+1
print(A)

A = "hello"
print(A) # A现在是字符串格式了，无法再参与运算，报错
#一次赋值多个变量，逗号隔开
b,c= 3,4
print("b =",b,"c =",c)
print(type(b))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))
print(isinstance(A,int))
print(type(A))

# 需求：现在又两个变量，分别为a和b，需要将两个变量值交换，然后输出到控制台

A = 10
B = 20
C = A
A = B
B = C
C = A
print("A =",A,"B =",B)
print("A =",A)
print("B =",B)