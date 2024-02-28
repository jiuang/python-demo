#!/usr/bin/python3
import csv  # 导入csv模块
import os

data2D = [
    [90, 98, 87],  # 第1名学生的3门课程成绩
    [70, 89, 92],  # 第2名学生的3门课程成绩
    [95, 78, 81],  # 第3名学生的3门课程成绩
    [98, 90, 95],  # 第4名学生的3门课程成绩
    [65, 72, 70]   # 第5名学生的3门课程成绩
]
file_name = os.getcwd() + os.sep + "data" + os.sep + "score.csv"

with open(file_name, 'a', newline='') as f:  # 打开文件
    csvwriter = csv.writer(f)  # 得到writer对象
    csvwriter.writerow(['语文', '数学', '英语'])  # 先将列标题写入CSV文件
    csvwriter.writerows(data2D)  # 将二维列表中的数据写入CSV文件
ls2 = []
with open(file_name, 'r', newline='') as f:  # 打开文件
    csvreader = csv.reader(f)  # 得到reader对象
    for line in csvreader:  # 将CSV文件中的一行数据作为列表读取到line中
        ls2.append(line)  # 将当前行数据的列表添加到ls2的尾部

for lx in ls2:
    print(lx)  # 输出ls2
