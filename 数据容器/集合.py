"""
"""
"""
集合set：无序的，不可重复、可修改的数据容器
自动去重，存储不重复元素

定义集合
s1 = {"a","b","c"}

定义空集合（不可以使用大括号！！！！单纯的大括号是字典）
s = set（）
"""

# s1 = {1,3,5,2,7,5,6,9}
# print(s1)

"""
集合的常见操作方法
1. add添加，将元素添加到集合中
2. remove 移除集合中的指定元素（如不存在将会报错）
3. pop 随机删除集合中的元素并返回
4. clear 清空集合
5. difference 取两个集合的差集（第一个减第二个集合）
取差集可以用-号直接计算
6. union 取并集
取并集不能用加号，而是|
7. intersection 取交集
取交集也可以用&直接计算

"""
# s1 = {1,3,5,2,7,5,6,9}
# s2 = {1,3,5,}
# s1.add(300)
# print(s1.difference(s2))
# print(s1.intersection(s2))

"""提供班级学生的选课情况，完成需求
1. 同时选了法语和艺术的学生
2. 同时选了4门课程的
3. 选了足球但没选篮球的
4. 统计每一个学生的选课数量
"""
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

# 选了法语和艺术
print(french_set.intersection(art_set))
print(french_set & art_set)

# 选了四门课程的
print(basketball_set.intersection(art_set, french_set,football_set))
# 选了足球没选篮球
print(football_set.difference(basketball_set))
print(football_set-basketball_set)
ft = {i for i in football_set if i not in basketball_set}
"推导式也能实现"
print(ft)


# 每个人分别选了多少课程
# list = football_set.union(basketball_set,french_set,art_set)
list = football_set | basketball_set | art_set | french_set

print(list)
print(type(list))
# for i in list:
#     a = 0
#     if i in basketball_set:
#         a += 1
#     if i in football_set:
#         a += 1
#     if i in art_set:
#         a += 1
#     if i in french_set:
#         a += 1
#     print(i,a)
all_list = [*football_set, *basketball_set, *art_set, *french_set]
for i in list:
    print(i,all_list.count(i))
