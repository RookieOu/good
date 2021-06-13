#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'商品分类-数据模型'



from App import  db
from sqlalchemy.dialects.postgresql import BOOLEAN,INTEGER,VARCHAR,JSONB,ARRAY
from sqlalchemy.sql import func,text
from sqlalchemy import Column,Table



#商品分类
class BUGOODSTYPE(db.Model):
    #表名
    __tablename__='bugoodstype'
    #id，主键，采用uuid
    id=db.Column(VARCHAR,primary_key=True)
    #商家id
    storeid=db.Column(VARCHAR)
    #名称
    name=db.Column(VARCHAR)
    #序号
    indexnum=db.Column(INTEGER)
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
                    'storeid':item.storeid,
                    'name':item.name,
                    'indexnum':item.indexnum,
                    'isdelete':item.isdelete
                    
                })
            return jsondata
        else:
            return {
                    'id':data.id,
                    'storeid':data.storeid,
                    'name':data.name,
                    'indexnum':data.indexnum,
                    'isdelete':data.isdelete
                }

def listdata():
    db.create_all()
