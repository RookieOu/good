#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'数据库视图'
__author__ = '黄洵斌'
__wdate__ = '2018/8/14'

from App import dbsession,  app
import asyncio
from flask import json, jsonify, g, request
from App.model.bugoodstype import BUGOODSTYPE
from App.util.security import getNewID

@app.route('/get_bugoodstype_data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_bugoodstype_data():
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
                BUGOODSTYPE).filter(BUGOODSTYPE.id.in_(ids['objectids'])).all(), default=BUGOODSTYPE.tojson))
        elif 'action' in argsdict and argsdict['action'] == 'get' and 'storeid' in argsdict and argsdict['storeid'] != "" :
            # 通过商家id获取商品类型列表
            data['data'] = json.loads(json.dumps(dbsession.query(
                BUGOODSTYPE).filter(BUGOODSTYPE.storeid==argsdict['storeid']).filter(BUGOODSTYPE.isdelete==False).order_by(BUGOODSTYPE.indexnum.asc()).all(), default=BUGOODSTYPE.tojson))
        
        elif 'action' in argsdict and argsdict['action'] == 'get':
            data['data'] = json.loads(json.dumps(dbsession.query(
                BUGOODSTYPE).all(), default=BUGOODSTYPE.tojson))
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
                newdata = BUGOODSTYPE(id=id, name=form['name'], storeid=form['storeid'], indexnum=form['indexnum'],isdelete=False)
                dbsession.add(newdata)
                dbsession.commit()
                data['data'] = json.loads(json.dumps(
                    BUGOODSTYPE.query.get(str(id)), default=BUGOODSTYPE.tojson))
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
                newdata=BUGOODSTYPE.query.get(str(form['id']))
                newdata.name=form['name']
                newdata.storeid=form['storeid']
                newdata.indexnum=form['indexnum']
                dbsession.commit()
                data['data'] = json.loads(json.dumps(
                    BUGOODSTYPE.query.get(str(form['id'])), default=BUGOODSTYPE.tojson))
            except Exception as e:
                # 生产上可以改为log
                print(e)
        else:
            code = 418
    elif method == 'DELETE':
        # 删除资源
        argsdict = dict(request.args)
        if 'id' in argsdict :
            deldata=BUGOODSTYPE.query.get(str(argsdict['id']))
            dbsession.delete(deldata)
            dbsession.commit()
            data['data'] = json.loads(json.dumps(deldata, default=BUGOODSTYPE.tojson))
        else:
            code = 418
    return jsonify(code=code, data=data, msg=msg)
