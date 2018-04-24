# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 16:38:37 2018

@author: zhangying
"""


import logging
import datetime
 

class MyLog():
    """程序调试日志输出"""
    
    
    def __init__(self,name,filepath):
        """初始化属性"""
        #初始化日志器
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        #初始化文件处理器
        #now = datetime.datetime.now()
        #time = (" " + str(now.hour) + "_" + 
                #str(now.minute) + "_" + str(now.second))
        #每天生成一个新的文件
        filepath = (filepath + "\\" + str(datetime.date.today()) +  " log.txt")
        self.fh = logging.FileHandler(filepath)
        self.fh.setLevel(logging.DEBUG)
        
        #初始化格式器
        self.formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                )
        
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        
        
    def getMyLogger(self):
        """获得自定义的日志器"""
        return self.logger