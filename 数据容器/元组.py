"""
"""

"""
列表list：元素可重复，有序，可修改
方括号[]
不适合需要记录不可修改只能查询的信息

元组tuple：元素可以重复、有序，不可修改
小括号()
支持索引访问，切片(切片仍要用方括号）
元组一旦被定义，不可修改

元组名称 = （元素1，元素2，……）
定义空元组
元组名称 = ()
元组名称 = tuple()

"""

"""元组操作方法
1. count- 统计某元素在元组中出现的次数
2. index- 查找某个元素在元组中第一次出现的索引位置
"""
# t = (22,345,45,67,80,92)
# print(type(t))
"定义单元素元组，元素后必须加逗号，否则不能成为元组"
# t1 = (99,)
# print(type(t1))

"切片仍然是方括号"
# print(t[0:3:1])
# print(t.index(22))

"""
元组的组包与解包
定义元组即为组包
"""
t = (22,345,45,67)
# 不加括号也能成为元组，但不推荐

"""解包
1. 基础解包，用与元组元素数量相同的变量一一接收元素
"""
# t = (22,345,45,67)
# a,b,c,d = t
# print(a,b,c,d)
"2. 扩展解包，用带*的变量接收剩余的多个元素"
# t = (22,345,45,67)
# a,*b,c = t
# print(a,b,c)
# print(b)
# print(type(b))

"完成a,b两个变量的交换"
# a = 10
# b = 20
# a,b = (b,a)
# # 这里括号可以省略
# print(a,b)

"""根据学生成绩单，完成如下需求（表格）
1. 计算每个学生的总分、各科平均分，然后输出
2. 统计各科成绩最低分、最高分、平均分并输出
3. 查找成绩优秀（均分大于90）的学生，并输出
"""
# 元组中可以嵌套元组
students = (
    ("s001","王林",85,92,78),
    ("s002","李慕婉",92,88,95),
    ("s002","十三",78,85,82)
)
# 计算每个学生的总分和平均分
# print("学号\t\t姓名\t\t总分\t\t平均分")
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total/3
#     print(f"{s[0]} \t {s[1]} \t {total}\t{avg:.1f}")
# avg后加:.1f保留1位小数，f的意思是指浮点数

# 获取各科的成绩，计算平均分最高分最低分
# chinese = [s[2] for s in students]
# math = [s[3] for s in students]
# english = [s[4] for s in students]
# print(f"语文最高分{max(chinese)},最低分{min(chinese)},平均分{sum(chinese)/len(chinese):.1f}")

# 获取优秀学生
# print("优秀学生名单")
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avg = total/3
#     if avg > 90:
#         print(f"{s[0]},{s[1]},{avg:.1f}")

"方式2，使用元组的解包来实现，这样通过不同变量来接收数据，避免使用索引来追踪数据，更直观"
print("优秀学生名单")
for id,name,chinese,math,english in students:
    total = chinese+math+english
    avg = total/3
    if avg > 90:
        print(f"{id},{name},{avg:.1f}")