"""条件控制语句：
1. 条件判断if,if……else，if……elif……else，
2. 模式匹配match……case
3. 循环
if 要判断的条件，条件必须为布尔值
if下第二行必须缩进，4个空格或一个tab
缩进来判断代码属于哪一个代码块，同一个块必须保持一致
"""

# 高考分高于600，能上一本
# score= int(input("请输入分数"))
# if score >= 600:
#     print("恭喜上一本")
#     print("请准备接收录取通知书")
# else :
#     print("再好好练练吧")

#输入账号密码判断登录
# acc = int(input("请输入账号"))
# password = int(input("请输入密码"))
#
# if acc == 123 and password == 456:
#     print("登陆成功")
# if acc != 123 or password != 456:
#     print("登录失败")

# if else,条件成立时执行if部分，不成立执行else部分
# acc = int(input("请输入账号"))
# password = int(input("请输入密码"))
#
# if acc == 123 and password == 456:
#     print("登陆成功")
# else:
#     print("登录失败")

"""需求：根据用户输入的年份，判断这一年是闰年还是平年
非整百年份，且能被4整除的是闰年，整百年份能被400整除的才是闰年
"""
# year = int(input("请输入年份"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("闰年")
# else:
#     print("平年")

# if, elif, else，多个条件判断，条件从上到下判断，不成立才会往下走


# # 判断输入数字是正数、负数还是0
# num= int(input("请输入数字"))
# if num > 0:
#     print("正数")
# elif num < 0:
#     print("负数")
# else:
#     print("0"

"""购物折扣计算，根据输入的总金额，以及下列折扣规则，计算实际应付金额
#大于等于500,8折，300到500,9折，100到300,95折，小于100无折扣
"""
# total = int(input("请输入总金额"))
# if total >= 500:
#     discount =0.8
#     total *= discount
#     print(f"您享受{10*discount}折优惠，总计应付{total}元")
# elif 300 <= total < 500:
#     discount = 0.9
#     total *= discount
#     print(f"您享受{10 * discount}折优惠，总计应付{total}元")
# elif 100 <= total < 300:
#     discount = 0.95
#     total *= discount
#     print(f"您享受{10 * discount}折优惠，总计应付{total}元")
# else :
#     print(f"您总计应付{total}元")
#
"""根据输入的3个数值，判定是否能组成三角形，如果能那么是等边，等腰还是普通三角形
#构成三角形的条件，任意两边之和大于第三边"""
# a = int(input("请输入第一条边长"))
# b = int(input("请输入第二条边长"))
# c = int(input("请输入第三条边长"))
# if a + b <= c or b + c <= a or a + c <= b:
#     print("无法组成三角形")
# elif a == b == c:
#     print("这是个等边三角形")
# elif a==b or b==c or c==a:
#     print("这是个等腰三角形")
# else:
#     print("这是个普通三角形")

"""阶梯电费计算
第一档2880度以下，电费单价0.4883
第二档2880到4800，单价0.5383
第三档4800以上，单价0.7883"""
sum = int(input("请输入用电量"))
if sum <= 2800:
    print(f"您的用电量处于第一档位，总计应付{sum*0.4883}元")
elif 2800 < sum <= 4800:
    print(f"您的用电量处于第二档位，总计应付{2800*0.4883+(sum-2800)*0.5383}元")
else:
    print(f"您的用电量处于第二档位，总计应付{2800 * 0.4883 + (4800 - 2800) * 0.5383+(sum-4800)*0.7883}元")