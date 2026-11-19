""""""
"""
Python模块：一个.py文件就是一个模块，模块式python程序的基本组织单位，在模块中可以定义变量、函数、累，以及可执行的代码
自定义模块+内置模块
内置模块：math(数学计算）, random（随机数）, os（操作系统）,sys（系统参数）等等

提高代码复用性，降低开发门槛，避免命名冲突

# 导入模块(写在所有代码之前)
导入模块的时候模块中的代码也会执行，在python中用特殊的内置变量来规避

特殊内置变量__name__，值为当前运行的模块的名称
通过if语句添加条件，使得模块测试代码仅在本模块执行时才运行
if __name__ == '__main__':
print('xxx')
如果被当做模块导入，则该代码不执行
python内置了功能，可以直接输入main来实现上述功能

特殊内置变量__all__
用于指定 from 模块名 import *时具体会导入哪些功能
在要导入的模块中定义__all__ = ["功能1","功能2","功能3"]
来限制*对应的范围

导入内置模块
1. 导入整个模块，调用需要模块名.功能名
    方法一：import random ,调用：random.randint(10,100)
    方法二（起个别名）：import random as rd ,调用：rd.randint(10,100)
2. 只导入模块中的部分功能，调用直接用功能名
    方法一：from random import randint,choice  调用：randint(10,100)
    方法二：from random import randint as rint  调用：rint(10,100)
    方法三：一次导入所有功能 from random import *  调用：randint(10,100)

导入自定义模块
模块名即文件名，建议使用python标识符定义，规范命名，不要用中文

Python软件包（package)
包：本质就是一个文件夹，该文件夹中可以包含若干python模块（.py文件），文件夹下还包含了一个__init__.py
__init__.py 也是py文件，有这个文件才是包
当模块文件较多时，用来管理多个模块，包的本质也是一个模块

导入方式及调用
1. import 包名.模块名
import utils.my_fun
调用：包名.模块名.功能名
2. from 包名 import 模块名
from utils import my_fun
调用：模块名.功能名
3. from 包名 import *      (导入包下的所有模块）
### 如果要通过这种模式导入所有模块，那么必须在__init__.py 中定义__all__ = ["模块1","模块2","模块3"]，否则会报错
调用：模块名.功能名
4. from 包名.模块名 import 功能名
from utils.my_fun import log_separator1
调用：功能名
5. from 包名.模块名 import *
from utils.my_fun import * (导入对应模块的所有功能）
调用：功能名

上述的包名都依赖于当前目录下，如果utils不在当前目录会报错，跨目录调用可以用绝对路径来定义，即从工程文件最高级一级一级.下来








"""




