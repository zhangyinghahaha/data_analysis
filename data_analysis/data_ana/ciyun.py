# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:33:42 2018

@author: ying.zhang01
"""

filename = "data_file\\ershoufang-clean-utf8-v1.1.csv"
miss_value = ["null","暂无数据"]
df_ershier = pd.read_csv(filename,skiprows=[0],na_values=miss_value)
df_ershier.comment.fillna(" ")
df_ershier.comment = df_ershier.comment.astype(str)

from wordcloud import WordCloud
import codecs
import jieba
#import jieba.analyse as analyse
from scipy.misc import imread
import os
from os import path
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


# 绘制词云
def draw_wordcloud():
    #读入一个txt文件
    comment_text = open("data_file\\ershoufang-clean-utf8-v1.1.csv",'r').read()
    #结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
    cut_text = " ".join(jieba.cut(comment_text))
    d = path.dirname(__file__) # 当前文件文件夹所在目录
    color_mask = imread("data_an\\beijing.jpg") # 读取背景图片
    cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        font_path="HYQiHei-25J.ttf",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=2000,
        #最大号字体
        max_font_size=40
    )
    word_cloud = cloud.generate(cut_text) # 产生词云
    word_cloud.to_file("pjl_cloud4.jpg") #保存图片
    #  显示词云图片
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()




    draw_wordcloud()