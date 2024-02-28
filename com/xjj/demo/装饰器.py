def decoration(f):
    def inner(x, y):
        print('decoration start...')
        f(x, y)
        print('decoration end...')

    return inner


@decoration
def testDecoration(x, y):
    print('我是业务代码……收到参数x=' + x + ', y=' + y)
