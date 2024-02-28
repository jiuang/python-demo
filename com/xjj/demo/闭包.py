# 闭包：一个函数里定义了一个内部函数，这个函数引用了外部函数的相关参数或变量，外部函数最终把这个内部函数返回了，那么这个内部函数被称为闭包
# 作用：闭包在运行时可以有多个实例，不同的引用环境和相同的函数组合可以产生不同的实例，这一点有点类似于面向对象中的类，其作用都是减少重复代码和提高功能的可扩展性
def func(x):
    print('x = ', x)
    def inner(y):
        print('y = ', y)
        return x + y
    return inner

def test闭包(x):
    # print(f)
    f = func(2)
    print(f(8))
    print(func(2)(8))