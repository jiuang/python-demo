# nonlocl
def nonlocl_outer():
    x = 10
    y = 10

    def nonlocl_inner():
        nonlocal x
        x = 20
        y = 20
        print('inner函数中的x, y变量值：', x, y)

    nonlocl_inner()  # 在outer函数中调用inner函数
    print('outer函数中的x, y变量值：', x, y)


def GlobalVar1():  # 定义函数GlobalVar1
    print('GlobalVar1中x的值为：', x)  # 输出全局变量x


def GlobalVar2():  # 定义函数GlobalVar2
    global x  # 通过global关键字声明在GlobalVar2函数中使用的是全局变量x
    x = 100  # 将全局变量x赋为100
    print('GlobalVar2中x的值为：', x)  # 输出全局变量x


x = 20  # 定义在所有函数之外，所以x是全局变量，赋为20

def testGlobalVariable():
    GlobalVar1()  # 调用GlobalVar1函数
    GlobalVar2()  # 调用GlobalVar2函数
    GlobalVar1()  # 调用GlobalVar1函数
