def 递归(n):
    if n == 1:
        return 1
    return n*递归(n - 1)


def add(f, x, y):
    return f(x) + f(y)

def square(x):
    return x**2

def 高阶函数(x, y):
    print(add(square, x, y))

def lambda简短函数(x, y):
    print(add(lambda x:x**2, x, y))