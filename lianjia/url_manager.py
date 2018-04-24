# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:00:43 2018

@author: zhangying
"""


class UrlManager():
    """url管理模块"""
    
    
    def __init__(self):
        """构造函数，初始化属性"""
        self.new_urls=set()     #新url的集合
        self.old_urls=set()     #旧的URL集合
    
    
    def add_new_url(self,url):
        """向管理器中添加一个URL"""
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    def add_new_urls(self,urls):
        """向管理器中添加批量URL"""
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)


    def get_new_url(self):
        """从url集合中弹出一个url"""
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
  

    def has_new_url(self):
        """判断是否还有新的url"""
        return len(self.new_urls) != 0