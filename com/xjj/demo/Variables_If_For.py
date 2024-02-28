def fun():
    x = 1
    print(id(x))

    x = 2
    print(id(x))

    a = "我是小写a变量"
    print(a)
    A = "我是大写A变量"
    print(A)

    a, b, c = 11, 22, 33
    print(a, b, c)

    if (x == 3):
        print("x = 3")
    elif (x == 4):
        print('x = ', x)
    else:
        print('x = ', x)

    for i in (2, 3, 5, 8):
        print('i = ', i)

    v = '哈哈哈'
    print('x = 1，变量x类型为：', type(x))
    print("v = '哈哈哈'，变量v类型为：", type(v))
