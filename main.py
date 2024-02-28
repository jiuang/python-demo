# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import numpy as np
# import sys

from com.xjj.demo import GlobalVariables, 高级函数, 闭包, 装饰器, 类与对象
from com.xjj.demo import GlobalVariables as QJBL
from com.xjj.demo.GlobalVariables import _a  # 直接导入某模块下的变量或函数

from com.xjj.demo import Collection, Function, String
from com.xjj.demo import 运算符与表达式
from com.xjj.demo import Variables_If_For
# from com.xjj.demo.Fruit import File
from com.xjj.demo.Fruit import Fruit
from com.xjj.demo import 关键字
from com.xjj.demo.类与对象 import CommonClass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# 测试中文注释

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print('time = ', time.time())

    # Variables_If_For.fun()

    # print(GlobalVariables._a)
    # print(QJBL._a)
    # print(_a)

    # 运算符与表达式.fun()

    # Collection.fun()

    # Function.fun()
    # print(Function.fun_with_return_value())
    # Function.fun_params('哈尔滨', 999999)
    # Function.test_range()
    # Function.fun_any_params('哈哈', 5, 8, "必须牛逼")

    # String.fun("尊重别人才是尊重自己", 45678)

    # File.write()
    # File.read()

    # Fruit.grow("我是")

    # 关键字.nonlocl_outer()
    # 关键字.testGlobalVariable()

    # print("递归函数测试：", 高级函数.递归(5))
    # 高级函数.高阶函数(2, 3)
    # 高级函数.lambda简短函数(2, 3)

    # 闭包.test闭包(2)

    # 装饰器.testDecoration('你好', '装饰器')

    # **************************____类与对象____***************************** start
    print('CommonClass.name = ', 类与对象.CommonClass.name)
    CommonClass.name = '张三'
    print('CommonClass.name = ', CommonClass.name)
    cmn = CommonClass()
    print('CommonClass().name = ', cmn.name)  # 从原 CommonClass 克隆出一个新对象
    cmn.name = '李四'
    print('CommonClass().name = ', cmn.name)

    print('CommonClass.name = ', CommonClass.name)

    cmn.age = 18
    cmn.adssdf = 20  # 该属性不被允许动态扩展
    print('CommonClass().age = ', cmn.age)

    CommonClass.commonClassMethod(CommonClass)
    cmn.commonClassMethod()

    del cmn  # 销毁s1对象

    print('s1对象已被销毁……')

    # 类与对象.CommonClass.testClassMethod(1, 2)
    # 类与对象.CommonClass.commonClassMethod(CommonClass())

    # 类与对象.testIsinstance()
    # 类与对象.testIssubclass()
    # 类与对象.testType()

    # **************************____类与对象____***************************** end


#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
