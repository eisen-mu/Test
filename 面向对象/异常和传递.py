""""""
"""
异常：程序运行中出现的错误，中断程序的正常执行流程
作用：保证数据、逻辑的正确性，避免程序执行混乱
在开发阶段尽量发现更多的问题，尽早解决问题，保障程序正常执行

处理方案：
1. 不做处理：整个程序出现bug后直接中断
2. 捕获异常：按照我们自己的处理方式处理异常，程序正常执行（编写程序的时候做好预案，出现异常时按预案处理

try:
    可能出现异常的代码1：
    可能出现异常的代码2：
    ...

except 异常类型 as 变量名(方括号内不写的话直接捕获所有异常
    出现异常时的预案

finally:(可选）
    不管是否出现异常，都会执行的代码
"""

# try:
#     print("===========")
#     print(1 / 0)
#     print(my_name)
#     print("+++++++++++")
# except NameError as a:
#     print(f"程序运行错误，{a}")
# except ZeroDivisionError as b:
#     print("零不能做除数")
# # 可以直接用Exception代替所有错误类型
# except Exception as e:
#     print("程勋运行出错",e)
# finally:
#     print("程序释放")

"""
异常的传递：异常在函数调用中层层上报，直到有人处理它或者程序崩溃

一般在主程序中捕获异常来处理
"""
def fun1():
    print("hello")
    fun2()

def fun2():
    print("hello")
    fun3()

def fun3():
    print("hello")
    print(color)

if __name__ == "__main__":
    # try:
        fun1()
    # except Exception as e:
    #     print(e)
