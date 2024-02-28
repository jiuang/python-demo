def fun():
    print('我是一个无参函数')

def fun_with_return_value():
    return '我是一个带有返回值的函数'

def fun_params(x, y):
    print('我是一个有参函数，x=', x, '，y=', y)

def fun_any_params(x, *args):
    print('我是不定参函数，x=', x, '，y=', args)

def test_range():
    print("range(1, 5, 2) 输出结果：", list(range(1, 5, 2)))
    print("range(1, 5) 输出结果：", list(range(1, 5)))
    print("range(5,-1,-2) 输出结果：", list(range(5, -1, -2)))
    print("range(5) 输出结果：", list(range(5)))
