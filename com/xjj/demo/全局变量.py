global user_id


def test001():
    globals()['user_id'] = '123'
    test002()


def test002():
    print("" + user_id)


test001()
