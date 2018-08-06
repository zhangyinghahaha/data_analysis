# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:22:06 2018

@author: zhangying
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

"""1、数据加载"""
#定义加载数据的文件名
#filename = "data_file\\ershoufang-mini-utf8.csv"
filename = "data_file\\ershoufang-clean-utf8-v1.1.csv"
#自定义数据的行列索引（行索引使用pd默认的，列索引使用自定义的）
names = [
        "id","communityName","areaName","total","unitPriceValue",
        "fwhx","szlc","jzmj","hxjg","tnmj",
        "jzlx","fwcx","jzjg","zxqk","thbl",
        "pbdt","cqnx","gpsj","jyqs","scjy",
        "fwyt","fwnx","cqss","dyxx","fbbj",
        ]
#自定义需要处理的缺失值标记列表
miss_value = ["null","暂无数据"]
#数据类型会自动转换
#使用自定义的列名，跳过文件中的头行，处理缺失值列表标记的缺失值
df = pd.read_csv(filename,skiprows=[0],names=names,na_values=miss_value)
#print(df.info())

"""2、数据运算"""
"""3、数据可视化呈现"""


"""南京二手房房屋用途占水平柱状图"""
count_fwyt = df["fwyt"].value_counts(ascending=True)
count_fwyt.name = ""

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_xlabel("房源数量(套)",fontsize=14)
ax.set_title("南京二手房房屋用途水平柱状图",fontsize=18)
count_fwyt.plot(kind="barh",fontsize=12)