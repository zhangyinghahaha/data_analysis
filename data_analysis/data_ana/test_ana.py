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
filename = "data_file\\ershoufang-mini-utf8.csv"
names = [
        "id","communityName","areaName","total","unitPriceValue",
        "fwhx","szlc","jzmj","hxjg","tnmj",
        "jzlx","fwcx","jzjg","zxqk","thbl",
        "pbdt","cqnx","gpsj","jyqs","scjy",
        "fwyt","fwnx","cqss","dyxx","fbbj",
        ]
df = pd.read_csv(filename,skiprows=[0],names=names)
#print(df.info())

mean_price_per_region = df.groupby(df.areaName)

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)

#,fontproperties="SimHei",fontsize=20
ax.set_title("南京各区域二手房平均价格")
mean_price_per_region.unitPriceValue.mean().plot.bar()
plt.savefig('data_ana\\picture\\mean_price.jpg')
plt.show()


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

df['fwhx'].value_counts()[:6].plot.pie(cmap=plt.cm.rainbow)
plt.savefig('data_ana\\picture\\房屋户型.jpg')
plt.title('房屋户型')

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
df.fwcx.value_counts()[:10].plot.bar()
plt.savefig('data_ana\\picture\\房屋朝向.jpg')
plt.title('房源朝向分布情况')