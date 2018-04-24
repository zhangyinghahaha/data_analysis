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