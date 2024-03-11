import queue


def put_queue(param):
    if q.qsize() == q.maxsize:
        q.get()
    q.put(param)


q = queue.Queue(maxsize=2)

if __name__ == '__main__':
    put_queue('a')
    put_queue('b')
    put_queue('c')
    # print(q.qsize())
    # 打印队列的内容
    while not q.empty():
        print(q.get())
    print(q.qsize())
