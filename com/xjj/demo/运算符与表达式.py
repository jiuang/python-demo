def fun():
    x = 1
    print(x + 1)
    print(x != 1)
    print(x == 1)
    print(x and 1)
    print(x or 1)
    print(1 / 2)

    print(eval("5*3.5+10"))  # eval内必须是字符串类型
    print(eval(input("请输入一个有效的表达式：")))

    x, y = 15, [3, 15, 8]
    print('x在y中：', (x in y))
