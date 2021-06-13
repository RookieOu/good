#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'商品-数据模型'


from App import  db
from sqlalchemy.dialects.postgresql import BOOLEAN,INTEGER,VARCHAR,JSONB,ARRAY,NUMERIC
from sqlalchemy.sql import func,text
from sqlalchemy import Column,Table



#数据库集群类
class BUGOODS(db.Model):
    #表名
    __tablename__='bugoods'
    #id，主键，采用uuid
    id=db.Column(VARCHAR,primary_key=True)
    #名称
    name=db.Column(VARCHAR)
    #商家id
    storeid=db.Column(VARCHAR)
    #分类id
    typeid=db.Column(VARCHAR)
    #价格
    price=db.Column(JSONB)
    #预库存
    prestockcount=db.Column(INTEGER)
    #实际库存
    stockcount=db.Column(INTEGER)
    #图片
    pics=db.Column(JSONB)
    #是否在售
    issaled=db.Column(BOOLEAN)
    #销量
    saledcount=db.Column(INTEGER)
    #规格
    standards=db.Column(JSONB)
    #折扣
    discount=db.Column(NUMERIC(3,1))
    #标签
    labels=db.Column(ARRAY(VARCHAR))
    #是否删除
    isdelete=db.Column(BOOLEAN)
    #允许配送时间
    delivery=db.Column(JSONB)
    
    #限购
    maxbuy=db.Column(INTEGER)
    #起购
    minbuy=db.Column(INTEGER)
    # 展示模块："1"为散客，“2”为团餐，“3”为两者都展示
    showmode=db.Column(VARCHAR)
    # 是否精选
    isselected=db.Column(BOOLEAN)
    # 是否热卖
    ishotsaled=db.Column(BOOLEAN)
    # 商品属性
    properties=db.Column(JSONB)
    # 企业版配送时间
    c_delivery=db.Column(JSONB)

    #将类实例数据转换为json格式
    #参数：用户实例
    def tojson(data):
        if type(data)==list:
            jsondata=[]
            for item in data:
                jsondata.append({
                    'id':item.id,
                    'typeid':item.typeid,
                    'price':item.price,
                    'prestockcount':item.prestockcount,
                    'stockcount':item.stockcount,
                    'name':item.name,
                    'pics':item.pics,
                    'issaled':item.issaled,
                    'saledcount':item.saledcount,
                    'standards':item.standards,
                    'discount':float(item.discount),
                    'labels':[x for x in item.labels],
                    'isdelete':item.isdelete,
                    'delivery':item.delivery,
                    'storeid':item.storeid,
                    'maxbuy':item.maxbuy,
                    'minbuy':item.minbuy,
                    'showmode':item.showmode,
                    'isselected':item.isselected,
                    'ishotsaled':item.ishotsaled,
                    'properties': item.properties,
                    'c_delivery':item.c_delivery
                })
            return jsondata
        else:
            return {
                    'id':data.id,
                    'typeid':data.typeid,
                    'price':data.price,
                    'prestockcount':data.prestockcount,
                    'stockcount':data.stockcount,
                    'name':data.name,
                    'pics':data.pics,
                    'issaled':data.issaled,
                    'saledcount':data.saledcount,
                    'standards':data.standards,
                    'discount':float(data.discount),
                    'labels':[x for x in data.labels],
                    'isdelete':data.isdelete,
                    'delivery':data.delivery,
                    'storeid':data.storeid,
                    'maxbuy':data.maxbuy,
                    'minbuy':data.minbuy,
                    'showmode':data.showmode,
                    'isselected':data.isselected,
                    'ishotsaled':data.ishotsaled,
                    'properties':data.properties,
                    'c_delivery':data.c_delivery
                }

def listdata():
    db.create_all()
