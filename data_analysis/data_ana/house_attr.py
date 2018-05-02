# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 15:21:27 2018

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


"""南京二手房房屋户型占比情况"""
count_fwhx = df['fwhx'].value_counts()[:10]
count_other_fwhx = pd.Series({"其他":df['fwhx'].value_counts()[10:].count()})
count_fwhx = count_fwhx.append(count_other_fwhx)
count_fwhx.index.name = ""
count_fwhx.name = ""

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
ax.set_title("南京二手房房屋户型占比情况",fontsize=18)
count_fwhx.plot(kind="pie",cmap=plt.cm.rainbow,autopct="%3.1f%%",fontsize=12)


"""南京二手房房屋装修占比情况"""
count_zxqk = df["zxqk"].value_counts()
count_zxqk.name = ""

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
ax.set_title("南京二手房装修占比情况",fontsize=18)
count_zxqk.plot(kind="pie",cmap=plt.cm.rainbow,autopct="%3.1f%%",fontsize=12)


"""南京二手房建筑类型占比情况"""
count_jzlx = df["jzlx"].value_counts()
count_jzlx.name = ""

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
ax.set_title("南京二手房建筑类型占比情况",fontsize=18)
count_jzlx.plot(kind="pie",cmap=plt.cm.rainbow,autopct="%3.1f%%",fontsize=12)


"""南京二手房房屋朝向分布情况"""
count_fwcx = df["fwcx"].value_counts()[:15]
count_other_fwcx = pd.Series({"其他":df['fwcx'].value_counts()[15:].count()})
count_fwcx = count_fwcx.append(count_other_fwcx)

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_title("房源朝向分布情况",fontsize=18)
count_fwcx.plot(kind="bar",fontsize=12)


"""南京二手房建筑面积分布区间"""
area_level = [0, 50, 100, 150, 200, 250, 300, 500]    
label_level = ['小于50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']    
jzmj_cut = pd.cut(df["jzmj"], area_level, labels=label_level)        
jzmj_result = jzmj_cut.value_counts()
#jzmj_result = jzmj_result.sort_values()

fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_ylabel("建筑面积(㎡)",fontsize=14)
ax.set_title("南京二手房建筑面积分布区间",fontsize=18)
jzmj_result.plot(kind="barh",fontsize=12)
