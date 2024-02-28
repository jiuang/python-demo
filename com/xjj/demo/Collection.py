arr = ('a', 'b', 'c')
list = ['aa', 'bb', 'cc']
map = {'a': 'aaa', 'b': 'bbb', 'c': 'ccc'}

def fun():
    for i in arr:
        print('arr = ', i)
    for i in list:
        print('list = ', i)
    for i in map:
        print('map = ', map.get(i))