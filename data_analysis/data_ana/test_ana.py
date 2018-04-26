# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:15:54 2018

@author: zhangying
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

"""1、数据加载"""
#定义加载数据的文件名
filename = "data_file\\ershoufang-mini-utf8.csv"
#filename = "data_file\\ershoufang-clean-utf8-v1.1.csv"

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

mean_price_per_region = df.groupby(df.areaName)

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)

#,fontproperties="SimHei",fontsize=20
ax.set_title("南京各区域二手房平均价格")
mean_price_per_region.unitPriceValue.mean().plot.bar()
#plt.savefig('data_ana\\picture\\mean_price.jpg')
plt.show()


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

df['fwhx'].value_counts()[:].plot.pie(cmap=plt.cm.rainbow)
#plt.savefig('data_ana\\picture\\房屋户型.jpg')
plt.title('南京二手房房屋户型分布')

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
df.fwcx.value_counts()[:10].plot.bar()
#plt.savefig('data_ana\\picture\\房屋朝向.jpg')
plt.title('房源朝向分布情况')