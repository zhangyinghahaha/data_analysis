# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:47:58 2018

@author: zhangying
"""

import numpy as np
import matplotlib.pyplot as plt

"""
plt.plot([1,2,3,4,5],[3,4,5,2,6])
plt.ylabel("grade")
#dpi图像质量，默认格式为png
#plt.savefig("first",dpi=600)
plt.axis([0,5,0,6])
plt.show()
"""

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

a = np.arange(0,5,0.02)
plt.subplot(211)
plt.plot(a,f(a))
plt.subplot(2,1,2)
plt.plot(a,np.cos(2*np.pi*a),"r--")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "STSong"
matplotlib.rcParams["font.size"] = 20

a = np.arange(0.0,5.0,0.02)

#输入中文
plt.xlabel("横轴：时间",fontproperties="SimHei",fontsize=20)
plt.ylabel("纵轴：振幅")
plt.plot(a,np.cos(2*np.pi*a),"r--")
plt.show()

#饼图
labels = "forgs","hogs","dogs","logs"
print(labels)
sizes = [15,30,45,10]
explode = (0,0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct="%1.1f%%",shadow=False,startangle=90)
plt.axis("equal")
plt.show()

#直方图
np.random.seed(0)
mu,sigma = 100,20
a = np.random.normal(mu,sigma,size=100)

plt.hist(a,10,normed=1,histtype="stepfilled",facecolor="b",alpha=0.75)
plt.show()

from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.print_echarts_options()
bar.render()

df1 = pd.DataFrame(np.arange(12.).reshape(3,4),columns=list("abcd"))
df1.plot(kind="box",fontsize=12)

data1 = {"key":["a","a","b","b"],"name":[1,2,3,4]}
frame1 = pd.DataFrame(data1)
seri = pd.Series([1,1,1,1])
seri.name = "name2"
frame1[seri.name] = seri

g = frame1["name"].groupby(frame1["key"])
g.size()

flag = 1

for f1,f2 in g:
    if flag == 1:
        re = pd.DataFrame(list(f2),columns=[f1])
        print(f1)
        print(f2)
        flag = 2
        continue
    re[f1] = list(f2)
    print(f1)
    print(f2)
    

data1 = [0,1,2,3]
data2 = [2,3,4,5]
arr1 = np.array(data1)
arr2 = np.array(data2)
np.sum(np.power(arr2-arr1, 2))

data3 = [[0,1,2,3],[2,3,4,5],[2,3,4,5]]
arr3 = np.array(data3)
index_a = arr3[:,1:3]
value = np.nonzero(index_a == 2)