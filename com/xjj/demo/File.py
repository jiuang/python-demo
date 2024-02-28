import os
# from numpy.core.setup_common import file

def read():
    file = open('d:\\a.txt', 'r')
    content = file.read()
    file.close()
    print(content)

def write():
    file = open('d:\\a.txt', 'w')
    file.write('测试python写文件内容')
    file.close()

def removeFile(file_path):
    try:
        # 判断文件是否存在
        if os.path.exists(file_path):
            # 如果文件存在则进行删除操作
            os.remove(file_path)
            print("文件[" + file_path + "]已成功删除！")
        else:
            print("文件[" + file_path + "]不存在，无法删除！")
    except Exception as e:
        print("删除文件[" + file_path + "]发生异常：", str(e))