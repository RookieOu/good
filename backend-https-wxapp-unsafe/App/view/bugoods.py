#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'数据库视图'
__author__ = '黄洵斌'
__wdate__ = '2018/8/14'

from App import dbsession,  app
import asyncio
from flask import json, jsonify, g, request
from App.model.bugoods import BUGOODS
from App.util.security import getNewID
from sqlalchemy import or_,and_

@app.route('/get_bugoods_data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_bugoods_data():
    # 初始化返回数据，规范为code/data/msg
    code = 200
    data = {
    }
    msg = ''
    method = request.method
    if method == 'GET':
        # GET方法需要判断action参数，action可以是get/handle，用于区分获取资源请求和操作请求
        argsdict = dict(request.args)
        
        if 'action' in argsdict and argsdict['action'] == 'get' and 'ids' in argsdict and argsdict['ids'] != "" :
            ids=json.loads(argsdict['ids'])
            data['data'] = json.loads(json.dumps(dbsession.query(
                BUGOODS).filter(BUGOODS.id.in_(ids)).all(), default=BUGOODS.tojson))
        elif 'action' in argsdict and argsdict['action'] == 'get' and 'isselected' in argsdict and argsdict['isselected'] ==True :
            # 精选商品
            data['data'] = json.loads(json.dumps(dbsession.query(
                BUGOODS).filter(BUGOODS.isselected==True).all(), default=BUGOODS.tojson))
        elif 'action' in argsdict and argsdict['action'] == 'get' and 'inited' in argsdict and argsdict['inited'] =='1' :
            # 小程序获取初始化商品=精选商品+购物车商品
            lovers=[x['goodsid'] for x in g.user.lovers['lovers']]
            # selectedgoods=dbsession.query( BUGOODS).filter(BUGOODS.isselected==True).all()
            # selectedgoodsids=[x.id for x in selectedgoods]
            # ids=list(set(lovers+selectedgoodsids))
            data['data'] = json.loads(json.dumps(dbsession.query(
                BUGOODS).filter(or_(BUGOODS.id.in_(lovers),BUGOODS.isselected==True)).all(), default=BUGOODS.tojson))
        elif 'action' in argsdict and argsdict['action'] == 'get' and 'storeid' in argsdict and argsdict['storeid'] != "" :
            # 根据商家查商品
            data['data'] = json.loads(json.dumps(dbsession.query(
                BUGOODS).filter(BUGOODS.storeid==argsdict['storeid']).all(), default=BUGOODS.tojson))
        elif 'action' in argsdict and argsdict['action'] == 'get' and 'typeid' in argsdict and argsdict['typeid'] != "" :
            # 根据分类查商品
            data['data'] = json.loads(json.dumps(dbsession.query(
                BUGOODS).filter(BUGOODS.typeid==argsdict['typeid']).all(), default=BUGOODS.tojson))
        elif 'action' in argsdict and argsdict['action'] == 'get':
            data['data'] = json.loads(json.dumps(dbsession.query(
                BUGOODS).all(), default=BUGOODS.tojson))
        elif 'action' in argsdict and argsdict['action'] == 'handle':
            pass
        else:
            code = 418
    elif method == 'POST':
        # 创建资源
        argsdict = json.loads(str(request.data, 'utf-8'))
        if 'form' in argsdict:
            form = argsdict['form']
            id = getNewID()
            try:
                newdata = BUGOODS(id=id, name=form['name'], typeid=form['typeid'],c_delivery=form['c_delivery'],
                                    price=form['price'], prestockcount=form['prestockcount'], 
                                    stockcount=form['stockcount'], pics=form['pics'],ishotsaled=form['ishotsaled'],isselected=form['isselected'],showmode=form['showmode'],properties=form['properties'],
                                     issaled=form['issaled'], saledcount=form['saledcount'],minbuy=form['minbuy'],maxbuy=form['maxbuy'],
                                      standards=form['standards'], discount=str(form['discount']), labels=form['labels'],delivery=form['delivery'],storeid=form['storeid'],isdelete=False)
                dbsession.add(newdata)
                dbsession.commit()
                data['data'] = json.loads(json.dumps(
                    BUGOODS.query.get(str(id)), default=BUGOODS.tojson))
            except Exception as e:
                # 生产上可以改为log
                print(e)
                code = 418
        else:
            code = 418
    elif method == 'PUT':
        # 更新资源
        argsdict = json.loads(str(request.data, 'utf-8'))
        if 'form' in argsdict:
            form = argsdict['form']
            try:
                newdata=BUGOODS.query.get(str(form['id']))
                newdata.name=form['name']
                newdata.typeid=form['typeid']
                newdata.price=form['price']
                newdata.prestockcount=form['prestockcount']
                newdata.stockcount=form['stockcount']
                newdata.pics=form['pics']
                newdata.issaled=form['issaled']
                newdata.saledcount=form['saledcount']
                newdata.standards=form['standards']
                newdata.discount=str(form['discount'])
                newdata.labels=form['labels']
                newdata.delivery=form['delivery']
                newdata.storeid=form['storeid']
                newdata.minbuy=form['minbuy']
                newdata.maxbuy=form['maxbuy']
                newdata.showmode=form['showmode']
                newdata.isselected=form['isselected']
                newdata.ishotsaled=form['ishotsaled']
                newdata.properties=form['properties']
                newdata.c_delivery=form['c_delivery']
                dbsession.commit()
                data['data'] = json.loads(json.dumps(
                    BUGOODS.query.get(str(form['id'])), default=BUGOODS.tojson))
            except Exception as e:
                # 生产上可以改为log
                print(e)
        else:
            code = 418
    elif method == 'DELETE':
        # 删除资源
        argsdict = dict(request.args)
        if 'id' in argsdict :
            deldata=BUGOODS.query.get(str(argsdict['id']))
            dbsession.delete(deldata)
            dbsession.commit()
            data['data'] = json.loads(json.dumps(deldata, default=BUGOODS.tojson))
        else:
            code = 418
    return jsonify(code=code, data=data, msg=msg)



@app.route('/get_bugoods_by_typeid', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_bugoods_by_typeid():
    # 初始化返回数据，规范为code/data/msg
    code = 200
    data = {
    }
    msg = ''
    method = request.method
    if method == 'GET':
        # GET方法需要判断action参数，action可以是get/handle，用于区分获取资源请求和操作请求
        argsdict = dict(request.args)
        
        if  'action' in argsdict and argsdict['action'] == 'get' and 'typeid' in argsdict and argsdict['typeid'] != "" :
            # 根据分类查商品

            sql="select * from bugoods where typeid="+argsdict['typeid']
            a=dbsession.execute(sql).fetchall()
            data['cdata_rows']=len(a)
            data['data']= json.loads(json.dumps(a, default=BUGOODS.tojson))
        else:
            code = 418
   
    return jsonify(code=code, data=data, msg=msg)
