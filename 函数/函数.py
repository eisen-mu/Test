""""""
"""
函数：组织好的，可复用的、用来实现特定功能的代码片段，只有调用时才会执行
函数定义与调用：
定义函数：

def 函数名（参数列表）：
    # (函数说明文档，用三引号括起来，可以用help调用)    
    
    函数体 
    ……
    return 返回值
#   return必须在最后，后面的不会执行
    
调用函数：
函数名（参数）    

函数定义括号内的的参数为形参，只能在函数内使用（局部变量）
调用函数时传入的参数为实参，需要与形参一一对应


"""
# # 定义
# def out_line():
#     print('_______')
# # 调用
# out_line()

'计算圆面积和周长'
def circle_area(r):
    area = 3.14 * r ** 2
    len = 2 * 3.14 * r
    return area,round(len,1)

'round(a,b),自带函数，将a保留b位小数'
'多个返回值用逗号分个，会封装在元组中返回'

# area,len = circle_area(3)
# print(area,len)
'计算长方形面积'
def rectangle_area(l,m):
    """
    计算长方形面积
    形参：长为l，宽为m
    返回值：面积
    """
    area = l * m
    return area
# area = rectangle_area(3,4)
# print(area)
#
# help(rectangle_area)

"""
函数的嵌套调用：在一个函数中调用了另一个函数
遵循栈结构，后进先出（LIFO，last in first out），最后被调用的最先返回
"""
"""
1. 定义一个函数，根据传入的底和高计算三角形面积
2. 定义一个函数，计算传入的字符串中的元音字母个数
3. 定义一个函数，计算传入的班级学员高潮成绩列表中的最高分、最低分和平均分（保留1位小数）
"""

def triangle(a,b):
    """
    计算三角形面积
    :param a: 三角形的底
    :param b: 三角形的高
    :return: 三角形面积
    """
    return a*b/2

def string(a):
    """    
    计算字符串中元音的数量
    :param a: 输入的字符串
    :return: 字符串中元音的数量
    """
    num = 0
    for i in a:
        # if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        if i in 'aeiouAEIOU':
            num += 1
    return num

def score(score_list):
    """
    计算传入列表中的最高分，最低分和平均分，
    :param score_list: 成绩列表
    :return: 最高分，最低分，平均分
    """
    a = max(score_list)
    b = min(score_list)
    c = sum(score_list)/len(score_list)
    return a,b,c

list = [589,577,623,344,678,435,264]
a,b,c = score(list)
print(a,b,round(c,2))
