#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'商家-数据模型'




from App import  db
from sqlalchemy.dialects.postgresql import BOOLEAN,INTEGER,VARCHAR,JSONB,ARRAY
from sqlalchemy.sql import func,text
from sqlalchemy import Column,Table



#商家类
class BUSTORE(db.Model):
    #表名
    __tablename__='bustore'
    #id，主键，采用uuid
    id=db.Column(VARCHAR,primary_key=True)
    #位置，经纬度
    site=db.Column(JSONB)
    #地址
    addr=db.Column(VARCHAR)
    #电话
    tel=db.Column(JSONB)
    #门店图片
    pic=db.Column(JSONB)
    #商标
    logo=db.Column(VARCHAR)
    #商圈id
    areaid=db.Column(VARCHAR)
    #品牌id
    brandid=db.Column(VARCHAR)
    #商家类别id
    typeid=db.Column(ARRAY(VARCHAR))
    #营业时间
    businessinfo=db.Column(JSONB)
    #名称
    name=db.Column(VARCHAR)
    #是否删除
    isdelete=db.Column(BOOLEAN)
    #负责人们
    manager=db.Column(ARRAY(VARCHAR))

    
    #将类实例数据转换为json格式
    #参数：用户实例
    def tojson(data):
        if type(data)==list:
            jsondata=[]
            for item in data:
                jsondata.append({
                    'id':item.id,
                    'site':item.site,
                    'addr':item.addr,
                    'tel':item.tel,
                    'pic':item.pic,
                    'name':item.name,
                    'logo':item.logo,
                    'areaid':item.areaid,
                    'brandid':item.brandid,
                    'businessinfo':item.businessinfo,
                    'isdelete':item.isdelete,
                    'typeid':[str(x) for x in item.typeid],
                    'manager':[str(x) for x in item.manager],
                    
                })
            return jsondata
        else:
            return {
                    'id':data.id,
                    'site':data.site,
                    'addr':data.addr,
                    'tel':data.tel,
                    'pic':data.pic,
                    'name':data.name,
                    'logo':data.logo,
                    'areaid':data.areaid,
                    'brandid':data.brandid,
                    'businessinfo':data.businessinfo,
                    'isdelete':data.isdelete,
                    'typeid':[str(x) for x in data.typeid],
                    'manager':[str(x) for x in data.manager],
                    
                }

def listdata():
    # db.drop_all()
    db.create_all()
