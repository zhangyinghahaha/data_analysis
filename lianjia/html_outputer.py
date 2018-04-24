# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:00:15 2018

@author: zhangying
"""


from log import MyLog 
import csv


class HtmlOutputer():
    """数据输出收集模块"""
    
    
    def __init__(self):
        """构造函数，初始化属性"""
        self.log = MyLog("html_outputer","logs")
        filename = "output\\ershoufang.csv"
        with open(filename,"w",newline="") as f:
            data = [
                    "id","小区名称","所在区域","总价","单价",
                    "房屋户型","所在楼层","建筑面积","户型结构",
                    "套内面积","建筑类型","房屋朝向","建筑结构",
                    "装修情况","梯户比例","配备电梯","产权年限",
                    "挂牌时间","交易权属","上次交易","房屋用途",
                    "房屋年限","产权所属","抵押信息","房本备件",
                    ]
            writer = csv.writer(f,dialect='excel')
            writer.writerow(data)
        
    
    def collect_data(self,data):
        if data is None:
            self.log.logger.error("页面数据收集：传入数据为空！")
            print("页面数据收集：传入数据为空！")
            return
        
        filename = "output\\ershoufang.csv"
        with open(filename,"a",newline="") as f:
            writer = csv.writer(f,dialect='excel')
            writer.writerow(data)
        
        self.log.logger.info("2.4页面数据收集：成功!")    
        print("2.4页面数据收集：成功!")