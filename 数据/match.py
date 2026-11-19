"""
match……case
从上往下依次匹配

"""

# 工作日程安排，周一到周日分别干啥
# day = input("请输入今天是周几（1-7）")
# match day:
#     case "1":
#         print("周一，工作会议日")
#     case "2":
#         print("周二，工作会议日")
#     case "3":
#         print("周三，工作会议日")
#     case "4":
#         print("周四，工作会议日")
#     case "5":
#         print("周五，工作会议日")

    # case _:
    #     # 这里下划线表示其他，相当于else
    #     print("周末，放假")

"""简易计算器
通过输入两个输，以及一个运算符，来实现四则运算
"""
a = float(input("请输入第一个数"))
b = float(input("请输入第二个数"))
c = input("请输入运算符")

match c:
    case "+":
        print(f"{a} + {b} = {a+b}")
    case "-":
        print(f"{a} - {b} = {a-b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "/":
        if b == 0:
            print("除数不能为0")
        else:
            print(f"{a} / {b} = {a / b}")
    # """这一段也可以写成下面这种形式
    # case "/" if b != 0:
    #     print(f"{a} / {b} = {a / b}")
    # 只有满足if条件才会匹配这条case
    # """

    case _:
        print("暂不支持这种计算")

"""根据输入指令，控制角色运动"""
oper = input("请输入操作: ")

match oper:
    # case使用|来同时匹配多个值，不能用or，只有case后面跟了if判断才可以在if中使用or
    case "w" | "W" | "上":
        print("角色向上移动")
    case "s" | "S" | "下":
        print("角色向下移动")
    case "a" | "A" | "左":
        print("角色向左移动")
    case "d" | "D" | "右":
        print("角色向右移动")
    case " " | "跳":
        print("角色跳跃")
    case "j" | "J" | "攻击":
        print("角色攻击")
    case "esc" | "ESC" | "退出":
        print("角色退出游戏")
    case _:
        print("非法操作, 不支持!!!")