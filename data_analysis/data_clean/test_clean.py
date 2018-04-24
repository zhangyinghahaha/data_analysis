# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:45:52 2018

@author: ying.zhang01
"""

#1、读入数据
#2、结构化数据
#3、查看需要处理的部分
#4、清理数据
#5、写出数据

import csv
filename = "data_file\\test.csv"
with open(filename,encoding="utf-8") as f:
    reader = csv.reader(f)
    context = [line for line in reader]

with open("data_file\\test1.txt","w",encoding="utf-8") as f:
    writer = csv.writer(f)    
    for line in context:
        line = [x.strip() for x in line]#去除每个数据项的空白符和换行符
        writer.writerow(line)