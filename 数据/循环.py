"""
while循环，for循环，嵌套循环
1. while循环
while 条件表达式：
    循环语句1
    循环语句2
else
条件表达式满足时才会执行while下面的循环。这个else可有可无

"""

# 打印10次“人生苦短，我用Python”
# i = 0
# while i < 10:
#     i += 1
#     print("人生苦短，我用Python")
# else:
#     print("打印完毕")

# 计算1-100之间所有偶数的累加之和
# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 2
# else:
#     print(sum)

"""
2. for循环
while循环是通过条件表达式来控制是否要进行下一次循环，如果一直满足就无限循环
for循环本质是一种轮询遍历机制，对一批内容逐个处理
for 元素 in 待处理数据集
    循环体代码
else
    循环结束时执行的代码
"""
# 遍历字符串
# msg = "Hello-Python"
# for i in msg:
#     print(f"元素:{i}")
# else:
#     print("循环结束")

"""
range语句，生成制定的数字序列
1. range(end)：获取一个从0开始，到end结束的整数序列，不包含end
range（5）就是01234
2. range(start，end):获取一个从start开始，到end结束的数字序列，不包含end
range(2,8)就是234567
3. range(start,end, step):获取一个从start开始，到end结束的数字序列，步长为step，不包含end
range(0,10,2)就是0,2,4,6,8

"""
# 基于for循环计算1-100内所有奇数之和
# sum = 0
# for i in range(1,101,2):
#     sum += i
# print(sum)
#
# sum = 0
# for i in range(0,101):
#     if i % 2 == 1:
#         sum += i
# print(sum)

"""基于for循环计算100-500内所有3的倍数之和"""
# sum = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         sum += i
# print(sum)
#
# sum = 0
# for i in range(102,501,3):
#     sum += i
# print(sum)

"""
3.嵌套循环
在循环的循环体中再嵌套循环

for 元素 in 待处理数据集1
    循环体代码1
    循环体代码2
    ……
    for 元素 in 待处理数据集2
    循环体代码1
    循环体代码2
"""

"""打印一个长度为m，宽度为n的长方形"""
# m = int(input("请输入长度m"))
# n = int(input("请输入宽度n"))
# for i in range(n):
#     for i in range(m):
#         print("*", end=" ")
#     print()
"""print自带换行效果，后面加end = “结束符”来确定结束符号"""

"""打印九九乘法表"""
# for i in range(1,10):
#     for j in range(1,i+1): #这里不能是1-10，否则每行都是打9个
#         print(f"{i}*{j}={i*j}",end="\t")
#         # 这里使用制表符可以统一格式
#         print()

"""打印等腰直角三角形"""
# A = int(input("请输入直角三角形边长"))
# for i in range(1,A+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

"""根据输入的数字，打印数字金字塔"""
# A = int(input("请输入数字"))
# for i in range(1,A+1):
#     for j in range(1,i):
#         print(" ", end=" ")
#     for j in range(i,A+1):
#         print(j,end=" ")
#     print()

"""打印国际象棋棋盘"""
# for i in range(1,9):
#     for j in range(1,9):
#         if i % 2 == 1:
#             if j % 2 == 1:
#                 print("■",end="  ")
#             else:
#                 print("□",end="  ")
#         else:
#             if j % 2 == 0:
#                 print("■",end="  ")
#             else:
#                 print("□",end="  ")
#     print()
"""这里用了太多的if，根据找规律，只要i+j能被2整除，那就是黑色，否则白色，可以大为简化"""
# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             print("■", end="  ")
#         else:
#             print("□", end="  ")
#     print()

"""根据输入的用户名和密码执行登录操作
1. 正确的用户名密码分别为admin/666888,zhangsan/123456,taoge/888666
2. 输入用户名和密码，登陆成功结束运行，登录失败则继续提示输入用户名和密码
3. 输入的用户名和密码不能为空
4. 登陆成功输出“登陆成功”
5. 登录失败输出“用户名或密码错误，请重新输入！”
"""
#
# s = 0
# "引入了s这个变量，显得冗杂，可以直接while True"
# while s == 0:
#
#     # 输入用户名和密码
#     user = input("请输入用户名")
#     password = input("请输入密码")
#     # 校验用户名密码是否为空
#     if user == "" or password == "":
#         print("输入不能为空，请重新输入！")
#         continue
#     """
#     continue表示终止当前循环，直接进入下一次循环
#     """
#     # 校验用户名和密码是否正确
#     if user =="admin" and password =="666888":
#         print("登陆成功")
#         s = 1
#         # break
#     elif user =="zhangsan" and password =="123456":
#         print("登陆成功")
#         s = 1
#         # break
#     elif user =="taoge" and password =="888666":
#         print("登陆成功")
#         s = 1
#         # break
#     else:
#         print("输入错误，请重新输入")

"""这里使用了s这个变量来控制循环状态，不太规范，实际上可以用break来终止循环，循环开始条件用while True就可以
break只能在循环中出现
如果使用了while else，break之后else部分不会执行"""

"""
猜数字
1. 系统生成一个随机数
2. 用户根据提示猜数字
3. 猜错了的话，系统提示猜大了还是小了，然后继续输入
4. 如果猜对了游戏结束

生成随机数需要先导入random模块，命令：
import random
random.randint(1,100)
生成1到100间的一个随机数，包含1和100
"""
import random
num = random.randint(1,100)
while True:
    A = int(input("请输入一个数字（1-100）"))
    if num == A:
        print(f"猜对了，数字是{num}")
        break
    elif num > A:
        print(f"小了")
    else:
        print(f"大了")




