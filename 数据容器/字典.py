""""""

"""
字典dict，存储键值对（key：value）类型的数据，可以根据键key找到对应的值value
定义:使用键值对存储数据，每一个键对应一个值，通过键可以快速找到对应的值
如果出现重复的键，那么后面的值会覆盖掉前面的值

字典名称 = {key: value, key:value,……}
定义空字典
字典名称 = {}

根据key取值(取值是中括号)
a = 字典名称[key]

注意！！！
字典的value可以是任何类型的数据
但key不可以是可变类型的数据（如不能为列表，集合、字典）

特点：键值对存储，键不能重复，值可以修改
"""
# dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
# print(dict1)
# print(dict1["王林"])
# dict1["李慕婉"] = 688
# print(dict1)
#
# dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688,"王林":700}
# print(dict1)
# # 重复键导致后面的值覆盖了前面的

"""
字典操作
1. 向字典中添加键值对
dict[key] = value
（如果不存在就添加，如果存在就修改）
2. 删除
dict.pop(key)
这种会删除对应的键值对，并返回这个key对应的value
del dict[key]
这种直接删除，不返回值
3. 查询
dict[key] 直接获取key
dict.get(key)  直接获取value
dict.keys() 获取所有的key
dict.values() 获取所有value
dict.items() 获取所有的键值对

"""
# dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}

# print(type(dict1.keys()))
# print(type(dict1.items()))

# 遍历输出
# 方法1
# for k in dict1.keys():
#     print(k,dict1[k])
# # 方法2
# for k,v in dict1.items():
#     print(k,v)

"""
案例:
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
    具体功能如下：
        1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
        5. 退出购物车

    结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}

"""
# shopping_cart = {}
# # alt + shift +鼠标选中多列，可移植性列编辑
# menu = """
# ########### 购物车系统 ##########
# #         1. 添加购物车         #
# #         2. 修改购物车         #
# #         3. 删除购物车         #
# #         4. 查询购物车         #
# #         5. 退出购物车         #
# ###############################
# """
# # 制作菜单
# print("欢迎使用购物车管理系统 ~")
# print(menu)
#
# # 执行操作
# while True:
#
#     choice = input("请选择你的操作")
#
#     match choice:
#         case "1":
#             name = input("请输入商品名称")
#
#             #     如果商品存在，报错
#             if name in shopping_cart:
#                 print("商品已存在，请重新添加")
#             else:
#                 price = float(input("请输入商品价格"))
#                 num = int(input("请输入商品数量"))
#                 shopping_cart[name] = {"price": price, "num": num}
#                 print("添加完成")
#
#         case "2":
#             name = input("请输入要修改的商品名称")
#
#             if name not in shopping_cart:
#                 print("该商品不存在，请重新输入")
#             else:
#                 shopping_cart[name] = {"price": price, "num": num}
#                 print("修改完成")
#         case "3":
#             name = input("请输入要删除的商品名称")
#             if name not in shopping_cart:
#                 print("该商品不存在，请重新输入")
#             else:
#                 del shopping_cart[name]
#                 print("删除完毕")
#         case "4":
#             total = shopping_cart.keys()
#             if not total:
#                 print("购物车是空的")
#             else:
#                 for name in shopping_cart.keys():
#                     info = shopping_cart[name]
#                     print(f"商品名称:{name}, 商品价格：{info["price"]}, 商品数量： {info["num"]}")
#         case "5":
#             print("885"
#                   "")
#             break
#
#         case _:
#             print("操作有误")


"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5. 列出所有学生：遍历所有学生信息并输出。
        6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7. 退出系统。
"""
menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎登入教务管理系统")
total_list = {}

while True:
    print(menu)
    choice = input("请选择你的操作")
    match choice:

        case "1":
            name = input("请输入学生姓名")
            if name in total_list.keys():
                print("学生信息已存在，请重新选择")
            else:
                chinese = int(input("请输入语文成绩"))
                math = int(input("请输入数学成绩"))
                english = int(input("请输入英语成绩"))
                total_list[name] = {"语文":chinese,"数学":math,"英语":english}
                print(total_list)
                print("成绩录入成功")


        case "2":
            name = input("请输入要修改的学生姓名")
            if name not in total_list:
                print("学生信息不存在，请重新选择")
            else:
                chinese = int(input("请输入语文成绩"))
                math = int(input("请输入数学成绩"))
                english = int(input("请输入英语成绩"))
                total_list[name] = {"语文": chinese, "数学": math, "英语": english}
                print("成绩录入成功")

        case "3":
            name = input("请输入要修改的学生姓名")
            if name not in total_list.keys():
                print("学生信息不存在，请重新选择")
            else:
                del total_list[name]
                print("删除成功")

        case "4":
            name = input("请输入要查询的学生姓名")
            if name not in total_list.keys():
                print("学生信息不存在，请重新选择")
            else:
                score = total_list[name]
                print(f"{name},语文成绩{score["语文"]}，数学成绩{score["数学"]},英语成绩{score["英语"]}")

        case "5":
            print(f"姓名\t 语文\t数学\t英语")
            for name in total_list.keys():
                score = total_list[name]
                print(f"{name} \t {score["语文"]}\t {score["数学"]}\t {score["英语"]}")

        case "6":
        #     先计算全班各科平均分，最高分和最低分
        #     chinese_list = {}
        #     math_list = {}
        #     english_list = {}
        # # 这里的方法把语数外成绩分别拆成3个字典了，其实没必要，可以用两个变量分别接收key和value，用value的字典直接找最大最小就行
        #     for name in total_list.keys():
        #         score = total_list[name]
        #         chinese_list[name] = score["语文"]
        #         math_list[name] = score["数学"]
        #         english_list[name] = score["英语"]
        #
        #     chinese = [*chinese_list.values()]
        #     math = [*math_list.values()]
        #     english = [*english_list.values()]
        #
        #     print(f"全班语文最高分{max(chinese)}，分别有")
        #     for name in chinese_list.keys():
        #         if chinese_list[name] == max(chinese):
        #             print(name)
        #     print(f"最低分{min(chinese)},分别有")
        #     for name in chinese_list.keys():
        #         if chinese_list[name] == min(chinese):
        #             print(name)
        #     print(f"平均分{sum(chinese)/len(chinese)}")
        #     print(f"全班数学最高分{max(math)}，最低分{min(math)},平均分{sum(math)/len(math)}")
        #     print(f"全班英语最高分{max(english)}，最低分{min(english)},平均分{sum(english)/len(english)}")
                # 初始化统计变量
            chinese_scores = []
            math_scores = []
            english_scores = []

                # 收集所有成绩
            for student_name, scores in total_list.items():
                chinese_scores.append(scores["语文"])
                math_scores.append(scores["数学"])
                english_scores.append(scores["英语"])
                # 找出最高分和最低分的学生
            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            chinese_avg = sum(chinese_scores) / len(chinese_scores)

            math_max = max(math_scores)
            math_min = min(math_scores)
            math_avg = sum(math_scores) / len(math_scores)

            english_max = max(english_scores)
            english_min = min(english_scores)
            english_avg = sum(english_scores) / len(english_scores)

            # 找出最高分和最低分的学生
            chinese_max_students = [name for name, scores in total_list.items() if scores["语文"] == chinese_max]
            chinese_min_students = [name for name, scores in total_list.items() if scores["语文"] == chinese_min]

            math_max_students = [name for name, scores in total_list.items() if scores["数学"] == math_max]
            math_min_students = [name for name, scores in total_list.items() if scores["数学"] == math_min]

            english_max_students = [name for name, scores in total_list.items() if scores["英语"] == english_max]
            english_min_students = [name for name, scores in total_list.items() if scores["英语"] == english_min]

            # 输出统计结果
            print("===== 班级成绩统计 =====")
            print(f"语文 - 最高分: {chinese_max}, 最低分: {chinese_min}, 平均分: {chinese_avg:.2f}")
            print(f"     最高分学生: {chinese_max_students}")
            print(f"     最低分学生: {chinese_min_students}")

            print(f"数学 - 最高分: {math_max}, 最低分: {math_min}, 平均分: {math_avg:.2f}")
            print(f"     最高分学生: {math_max_students}")
            print(f"     最低分学生: {math_min_students}")

            print(f"英语 - 最高分: {english_max}, 最低分: {english_min}, 平均分: {english_avg:.2f}")
            print(f"     最高分学生: {english_max_students}")
            print(f"     最低分学生: {english_min_students}")
            print("========================")

        case _:
            print("操作有误，请重新输入")






