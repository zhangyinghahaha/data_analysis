# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:58:57 2018

@author: zhangying
"""

import url_manager, html_downloader, html_parser, html_outputer,utill

class SpiderMain(object):
    #构造函数，初始化各个对象
    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
        self.util=utill.DBConn()

    #爬虫主函数
    def craw(self,root_url):
        #限定爬取次数
        count = 1
        flag = 0
        
        #初始化URL管理器
        #while count < 10:
            #urladd = root_url + str(count)
            #self.urls.add_new_url(urladd)
            #print("已经向URL管理器中添加id= %d 的URL"% count)
            #count = count + 1
        #添加到root URL管理器中
        #self.urls.add_new_url(root_url)
        #启动爬虫循环,如果URL管理器中不为空，就一直执行
        while count < 57:
            try:
                
                #获取一个新的链接
                new_url = root_url + str(count)
                #控制台打印本次爬取序号以及链接
                print("\n正在爬取: %s"% new_url)
                #启动下载器,下载页面.
                html_cont = self.downloader.download(new_url)
                #调用解析器解析页面,得到新的URL、数据
                pest = self.parser.parse(new_url,html_cont,count)
                
                #添加新的url链接到URL管理器
                #self.urls.add_new_urls(new_urls)
                try:
                    #收集到的数据输出到html中
                    rs = self.util.getRS()
                    self.outputer.collect_data(rs,pest)
                except:
                    print("数据入库失败")
                    flag = flag + 1
                    if flag == 5:
                        flag = 0
                        count = count + 1
                    continue
                finally:
                    rs.close()
                    
                count = count + 1
            except:
                count = count + 1
                print('页面爬取失败（）!!!')
"""
if __name__ == "__main__":
    #设定爬虫入口URL
    root_url = "http://pests.agridata.cn/show3.asp?DB=1&id="
    
    #初始化爬虫对象
    obj_spider = SpiderMain()
    #启动爬虫
    obj_spider.craw(root_url)
"""