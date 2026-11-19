"""
"""
"""
字符串：字符的容器，一个字符串可以存放任意数量的字符
特点：不可变性（无法修改）、有序性、可迭代性（可以通过for循环依次取出）
索引：字符串中每一个字符元素都有对应下标，和列表一样，从0开始，也支持倒序（最后一个是-1）
基本操作：
1. 切片，与列表一致
序列对象[开始索引：结束索引：步长]
（不包含结束索引）
"""
# s = "hello-world"
# print(s[6])
# print(s[0:6:])
# print(s[::-1])
# # 字符串不可变，无法进行赋值操作
# for i in s:
#     print(i)

"""常用方法
1. find-在字符串里查找字串，返回第一次出现的索引位置，找不到返回-1
s.find("abc")
2. count-统计子串在字符串中出现的次数
s.count("abc")
3. upper-将所有字母转换为大写
s.upper()
4. lower-将所有字母转换为小写
s.lower()
5. split-将字符串按照指定分隔符切成列表
s.split("-")
6. strip- 去除字符串来年高端的空白字符或指定字符(参数不指定默认去除空格)
s.strip() 或 s.strip("*")
7. replace- 将字符串中的指定子串替换为新的子串
s.replace("*","A")
8. startwith- 检查字符串是否以指定子串开头，返回布尔值
s.startwith("A")
9. endwith- 检查是否以指定字符串结束
s.endwith("A")

"""
# s = "hello-world"
# c = s.find("e")
# print(s.find("e"))
# print(c)
# d = s.count("o")
# print(d)
# e = s.split("-")
# print(e)
# print(type(e))
# f = s.strip("d")
# print(f)
# g = s.replace("o","*")
# print(g)
# h = s.startswith("*")
# print(h)
# i = s.upper()
# print(i)
# print(s)

"""邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含唯一一个@和至少一个.），如果输入正确，输出\”邮箱格式正确\“，否则输出邮箱格式错误
"""
# 方法1
# mail = input("请输入邮箱地址")
# a = mail.count("@")
# b = mail.count(".")
# # 没必要用引入变量，可以直接用表达式和固定值比较
# # 例如
# # mail.count("@") == 1
# if a == 1 and b >= 1:
#     print("正确")
# else:
#     print("错误")
# 方法2
# mail = input("请输入邮箱地址")
# if "." in mail and mail.count("@") == 1:
#     print("正确")
# else:
#     print("错误")
#
# """输入一个字符串，判断该字符串是否是回温（对称）"""
# s = input("请输入字符串")
# if s == s[::-1]:
#     print("是回文")
# else:
#     print("不是回文")

"""将用户输入的10个字符串反转后全部转换为大写，然后记录在列表中，最后将列表内容遍历输出出来"""
s = []
for i in range(3):
    a = input("请输入内容")
    # b = a[::-1]
    # s.append(b.upper())
# 这里表达式可以连着用
    s.append(a[::-1].upper())
for i in s:
    print(i)


