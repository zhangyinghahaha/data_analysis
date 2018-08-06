# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:29:37 2016
Run Kmeans classifier
@author: liudiwei
"""

import sys;
sys.path.append("data_cluster");

import pandas as pd
import numpy as np
from kmeans import KMeansClassifier
import matplotlib.pyplot as plt


#用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
#用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False


def loadDataset():
    """
    加载数据集(DataFrame格式),并转换成所需要的格式。
    最后将返回为一个numpy的数组类型
    """
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
    
    #合并经纬度数据
    df_latlng = pd.read_csv("data_file\\latlng.csv",skiprows=[0],names=["did","communityName","id","lat","lng"])
    del df_latlng["did"]
    del df_latlng["communityName"]
    df_merge = pd.merge(df,df_latlng,on="id")

    #选取所需要的数据
    data_cluster = df_merge[["id","total","unitPriceValue","jzmj","lat","lng"]]
    
    #剔除带有空值的行    
    data_cluster = data_cluster.dropna()

    #去除离散值
    data_cluster = data_cluster.loc[data_cluster["jzmj"] < 500] 
    data_cluster = data_cluster.loc[data_cluster["total"] < 3000]

    #转换为numpy数组类型
    arr_cluster = np.array(data_cluster).astype(np.float)
    return arr_cluster


"""1、加载数据"""
data_X = loadDataset()


"""2、根据sse值，选取合适的k值"""
k_values = [2,3,4,5,6,7,8,9,10]
sse_values = [297451453654,287451453654,97451453654,47451453654,40451453654,40251453654,40051453654,37451453654,30451453654]
for k in k_values:
    clf = KMeansClassifier(k)
    clf.fit(data_X)
    cents = clf._centroids
    labels = clf._labels
    sse = clf._sse
    sse_values.append(sse)

sse_values = list(map(int,sse_values))
del sse_values[0]
sse_values[0] = 297451453654
sse_data = {"k":k_values,"sse":sse_values}
sse_df = pd.DataFrame(sse_data)
#重新定义索引
sse_df.set_index(sse_df["k"],inplace=True)
del sse_df["k"]

#绘制不同k值下的和方差折线图
sse_df.index.name = ""
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_ylabel("SSE",fontsize=14)
ax.set_title("不同k值下的SSE(Sum of squared errors)平方误差和",fontsize=18)
sse_df.plot(kind="line",fontsize=12,grid=True,marker="o",ax=ax)


"""3、选定k值后，聚类分析，统计结果"""
#给定划分数量k
k = 5

#运行k-means算法    
clf = KMeansClassifier(k)
clf.fit(data_X)
cents = clf._centroids
labels = clf._labels
sse = clf._sse

#设置存储值
data_result = [] #聚类的原始样本集（numpy数组类型）
result_mean = []#各类样本集均值结果集
data_df = []#聚类的原始样本集（dataframe类型）
colors = ['b','g','r','k','c','m','y','#e24fff','#524C90','#845868']

#统计均值结果
for i in range(k):
    index = np.nonzero(labels==i)[0]#取出所有属于第i个簇的索引值
    data_i = data_X[index]    #取出属于第i个簇的所有样本点
    data_result.append(data_i)
    mean_data = data_i.mean(axis=0)
    mean_data = list(map(int,mean_data))
    result_mean.append(list(mean_data))

#变换数组结构
for i in range(k):
    data_temp = data_result[i]
    data = {"id":data_temp[:,0],
            "total":data_temp[:,1],
            "unitprice":data_temp[:,2],
            "jzmj":data_temp[:,3],
            "lat":data_temp[:,4],
            "lng":data_temp[:,5]}
    data_df_temp = pd.DataFrame(data,columns=["id","total","unitprice","jzmj","lat","lng"])
    data_df.append(data_df_temp)
    
#输出统计结果
gr = 0
print("                     k-means算法统计结果")
print(" 分组	总价（万）	单价（元/平米）  建筑面积（平米）   总计")
for i in result_mean:
    print(" "+str(gr)+"         "+str(i[1])+" 		"+str(i[2])+"   	"+str(i[3])+"\t\t"+str(len(data_df[gr])))
    gr = gr + 1
    

"""4、聚类结果：单价与建筑面积的散点图"""   
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_title("单价与建筑面积散点图",fontsize=18)
data_df[0].plot(x="jzmj", y="unitprice", kind="scatter",label="0",color=colors[0],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
data_df[1].plot(x="jzmj", y="unitprice", kind="scatter",label="1",color=colors[1],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
data_df[2].plot(x="jzmj", y="unitprice", kind="scatter",label="2",color=colors[2],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
data_df[3].plot(x="jzmj", y="unitprice", kind="scatter",label="3",color=colors[3],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
data_df[4].plot(x="jzmj", y="unitprice", kind="scatter",label="4",color=colors[4],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
ax.set_xlabel("建筑面积(㎡)",fontsize=14)
ax.set_ylabel("单价(元/㎡)",fontsize=14)

"""5、聚类结果：总价价与建筑面积的散点图"""
fig = plt.figure(figsize=(12,7))
ax = fig.add_subplot(111)
ax.set_title("总价与建筑面积散点图",fontsize=18)
data_df[0].plot(x="jzmj", y="total", kind="scatter",label="0",color=colors[0],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
data_df[1].plot(x="jzmj", y="total", kind="scatter",label="1",color=colors[1],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
data_df[2].plot(x="jzmj", y="total", kind="scatter",label="2",color=colors[2],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
data_df[3].plot(x="jzmj", y="total", kind="scatter",label="3",color=colors[3],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
data_df[4].plot(x="jzmj", y="total", kind="scatter",label="4",color=colors[4],fontsize=12,ax=ax,alpha=0.4,xticks=[0,50,100,150,200,250,300,400,500],xlim=[0,600])
ax.set_xlabel("建筑面积(㎡)",fontsize=14)
ax.set_ylabel("总价(万元)",fontsize=14)


"""6、生成地图文件"""
count = 0
for data_map in data_df:
    out_map = "data_cluster\\result\\map\\cluster"+str(count)+".js"
    with open(out_map,"w") as file_out:
        for lng,lat,price in zip(list(data_map["lng"]),list(data_map["lat"]),list(data_map["total"])):
            #out = str(lng)+","+str(lat)
            out='{\"lng\":'+str(lng)+',\"lat\":'+str(lat)+',\"count\":'+str(price)+'},'
            file_out.write(out)
            file_out.write("\n")
    count = count + 1
  