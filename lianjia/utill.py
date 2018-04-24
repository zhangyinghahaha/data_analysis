# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:00:55 2018

@author: zhangying
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建对象的基类:
Base = declarative_base()
#数据库连接
class DBConn(object):
    #构造函数，初始化各个对象
    def __init__(self):
        #初始化数据库连接:
        self.engine = create_engine('mysql+pymysql://root:123456@localhost:3306/pest?charset=utf8')
        # 创建DBSession类型:
        self.RiceSession = sessionmaker(bind=self.engine)
        self.rs = self.RiceSession()

    def getRS(self):
        return self.rs

#小麦基本信息表（46）
class Pest(Base):
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }

    __tablename__ = 't_rice_pest'

    id = Column(Integer, primary_key=True)
    
    jiluhao= Column(String(200))
    zhongwenming= Column(String(200))
    ldxm= Column(String(200))
    gang= Column(String(200))
    mu= Column(String(200))
    
    ke= Column(String(200))
    tiandi= Column(String(200))
    zywhzw= Column(String(200))
    xttz= Column(String(6000))
    swxtxjfsxzgl= Column(String(200))
    
    fzff= Column(String(200))
    dlfb= Column(String(200))
    xgwx= Column(String(200))
