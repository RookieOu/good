#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'商家分类-数据模型'

__author__='黄洵斌'
__wdate__='2019/5/26'

from App import  db
from sqlalchemy.dialects.postgresql import BOOLEAN,INTEGER,VARCHAR,JSONB,ARRAY
from sqlalchemy.sql import func,text
from sqlalchemy import Column,Table



#商家分类
class BUSTORETYPE(db.Model):
    #表名
    __tablename__='bustoretype'
    #id，主键，采用uuid
    id=db.Column(VARCHAR,primary_key=True)
    #名称
    name=db.Column(VARCHAR)
    #是否删除
    isdelete=db.Column(BOOLEAN)

    #将类实例数据转换为json格式
    #参数：用户实例
    def tojson(data):
        if type(data)==list:
            jsondata=[]
            for item in data:
                jsondata.append({
                    'id':item.id,
                    'name':item.name,
                    'isdelete':item.isdelete
                })
            return jsondata
        else:
            return {
                    'id':data.id,
                    'name':data.name,
                    'isdelete':data.isdelete
                }

def listdata():
    db.create_all()
