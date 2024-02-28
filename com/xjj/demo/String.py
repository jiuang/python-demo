def fun(str1, num):
    format_str = "%s--%d" % (str1, num)  # 注意此处的占位符%s代表字符串、%d代表数字、%f代表浮点数
    print('字符串格式化输出：', format_str)

    str1 = "hello "
    str2 = "world"
    print('字符串相加：', str1 + str2)

    print('字符串长度：', len(str2))

    word = "world"
    print('字符串截取：', word[0:3])
    print('字符串截取：', word[3])
    print('字符串截取：', word[3:len(word)])
