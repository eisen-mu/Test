""""""
from unittest import case

"""
采用面向对象的方法，完成教务管理系统的开发，教务管理系统可以管理在校学生的成绩，通过控制台菜单与用户交互，功能如下：
1. 添加学生成绩：根据输入的学生姓名、鱼粉成绩、数学成绩、英语成绩，记录在系统中
2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
4. 查询指定的学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
5. 展示全部学生成绩
"""

# 分析，定义两个类，一个是学生，一个是教务系统
# 学生类用来管理成绩
# 功能1-5都是教务系统的方法
# 先定义学生类
class Student:
    def __init__(self, name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分： {self.chinese +self.math +self.english}"
    # 定义修改学生成绩的方法
    def update_score(self,chinese = None, math = None, english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
# 定义教务管理系统类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []
    # 列表，只有添加学生成绩的时候才会把学生对象传递进来
    # 添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名：")
    # 判断学生的姓名是否存在，如果存在提示添加失败
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在，添加失败")
                return

        chinese = int(input("请输入语文成绩："))
        math = int(input("请输入数学成绩:"))
        english = int(input("请输入英语成绩:"))
        # 判断分数是否在0-100之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功")
        else:
            print("学生成绩必须在0-100之间")

#   修改学生成绩
    def update_student(self):
        name = input("请输入学生姓名：")
        # 判断学生的姓名是否存在，如果存在提示添加失败
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")
                chinese = int(input("请输入语文成绩："))
                math = int(input("请输入数学成绩:"))
                english = int(input("请输入英语成绩:"))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功")
                    print(f"修改后的成绩为：{s}")
                    return
                else:
                    print("学生成绩必须在0-100之间")
                    return
        print("未找到该学生，修改失败")
#   删除学生成绩
    def delete_student(self):
        name = input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
        print("未找到该学生，删除失败")

#   查询指定学生成绩
    def query_student(self):
        name = input("请输入学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息：{s}")
                return
        print("未找到该学生，查询失败")
#   罗列所有学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)
#   运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")
        while True:
            print()
            print("###############################")
            print("#1. 添加学生 2.修改学生 3. 删除学生 4. 查询指定学生 5. 查询所有学生 6. 退出系统#")
            print("###############################")

            choice = int(input("请选择要执行的操作，输入1-6"))
            match choice:
                case 1: #添加学生
                    self.add_student()
                case 2: #修改学生
                    self.update_student()
                case 3: #删除学生
                    self.delete_student()
                case 4:
                    self.query_student()
                case 5:
                    self.list_student()
                case 6:
                    break
                case _:
                    print("请输出正确的数字")



# 测试
if __name__ == "__main__":
    edu_management = EduManagement()
    edu_management.run()
#     s1 = Student("王琳",90,88,92)
#     print(s1)
#     s1.update_score(english=95)
#     print(s1)