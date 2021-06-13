#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'数据库视图'
__author__ = '黄洵斌'
__wdate__ = '2018/8/14'

from App import dbsession,  app
import asyncio
from flask import json, jsonify, g, request
from App.model.bustore import BUSTORE
from App.util.security import getNewID
from sqlalchemy.orm.attributes import flag_modified
from math import radians, cos, sin, asin, sqrt
from sqlalchemy import all_,any_
from App.model.base_role import BASEROLES


@app.route('/get_bustore_data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_bustore_data():
    # 初始化返回数据，规范为code/data/msg
    code = 200
    data = {
    }
    msg = ''
    method = request.method
    # 鉴权
    allprivs=[]
    roledatas=json.loads(json.dumps(dbsession.query(
                BASEROLES).all(), default=BASEROLES.tojson))
    for role in g.user.roles:
        privs=list(filter(lambda x:x['id']==role,roledatas))
        if privs!=[]:
            allprivs=allprivs+privs[0]['privs']
    if "商家" not in list(set(allprivs)):
        code=418
        msg="对不起，你没有权限访问"
        return jsonify(code=code, data=data, msg=msg)

    if method == 'GET':
        # GET方法需要判断action参数，action可以是get/handle，用于区分获取资源请求和操作请求
        argsdict = dict(request.args)
    
        if 'action' in argsdict and argsdict['action'] == 'get':
            query=dbsession.query(BUSTORE)
            
            if 'ids' in argsdict and argsdict['ids'] != "" :
                if 'limit' in argsdict and int(argsdict['limit']) !=0 and 'offset' in argsdict :
                    query=query.offset(int(argsdict['offset'])).limit(argsdict['limit'])
                ids=json.loads(argsdict['ids'])
                query=query.filter(BUSTORE.id.in_(ids['objectids'])).all()
            else:
                if  'areaid' in argsdict and argsdict['areaid'] != "" :
                    query=query.filter(BUSTORE.areaid==argsdict['areaid'])
                if  'typeid' in argsdict and argsdict['typeid'] != "" :
                    query=query.filter(any_(BUSTORE.typeid)==argsdict['typeid'])
                if  'searchvalue' in argsdict and argsdict['searchvalue'] != "" :
                    # 关键字搜索
                    # 后续增加商家类型和相关性的搜索

                    query=query.filter(BUSTORE.name.like("%"+argsdict['searchvalue']+"%") )
                
                
                if 'limit' in argsdict and int(argsdict['limit']) !=0 and 'offset' in argsdict :
                    query=query.offset(int(argsdict['offset'])).limit(argsdict['limit'])
                query=query.all()
            
            data['data'] =json.loads(json.dumps(query, default=BUSTORE.tojson))
                
        else:
            code = 418
        
    elif method == 'POST':
        # 创建资源
        argsdict = json.loads(str(request.data, 'utf-8'))
        if 'form' in argsdict:
            form = argsdict['form']
            id = getNewID()
            try:
                newdata = BUSTORE(id=id, name=form['name'], site=form['site'],
                                    addr=form['addr'], tel=form['tel'], 
                                    pic=form['pic'], logo=form['logo'],
                                     areaid=form['areaid'], brandid=form['brandid'],
                                      businessinfo=form['businessinfo'], typeid=form['typeid'],manager=form['manager'], isdelete=False)
                dbsession.add(newdata)
                dbsession.commit()
                data['data'] = json.loads(json.dumps(
                    BUSTORE.query.get(str(id)), default=BUSTORE.tojson))
            except Exception as e:
                app.logger.error(e)
                code = 418
        else:
            code = 418
    elif method == 'PUT':
        # 更新资源
        argsdict = json.loads(str(request.data, 'utf-8'))
        if 'form' in argsdict:
            form = argsdict['form']
            try:
                newdata=BUSTORE.query.get(str(form['id']))
                newdata.name=form['name']
                newdata.site=form['site']
                newdata.addr=form['addr']
                newdata.tel=form['tel']
                newdata.pic=form['pic']
                newdata.logo=form['logo']
                newdata.areaid=form['areaid']
                newdata.brandid=form['brandid']
                newdata.businessinfo=form['businessinfo']
                newdata.typeid=form['typeid']
                newdata.manager=form['manager']
                dbsession.commit()
                data['data'] = json.loads(json.dumps(
                    BUSTORE.query.get(str(form['id'])), default=BUSTORE.tojson))
            except Exception as e:
                app.logger.error(e)
        else:
            code = 418
    elif method == 'DELETE':
        # 删除资源
        argsdict = dict(request.args)
        if 'id' in argsdict :
            deldata=BUSTORE.query.get(str(argsdict['id']))
            dbsession.delete(deldata)
            dbsession.commit()
            data['data'] = json.loads(json.dumps(deldata, default=BUSTORE.tojson))
        else:
            code = 418
    return jsonify(code=code, data=data, msg=msg)



@app.route('/get_bustore_addpic', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_bustore_addpic():
    # 初始化返回数据，规范为code/data/msg
    code = 200
    data = {
    }
    msg = ''
    method = request.method
    if method == 'PUT':
        # 更新资源
        argsdict = json.loads(str(request.data, 'utf-8'))
        if 'form' in argsdict :
            form = argsdict['form']
            if 'id' in form and 'newpic' in form and 'area' in form:
                try:
                    newdata=BUSTORE.query.get(str(form['id']))
                    if str(form['area'])== 'store':
                        newdata.pic['storepic'].append(form['newpic'])
                        flag_modified(newdata, "pic")
                        dbsession.commit()
                    elif str(form['area'])== 'goods':
                        newdata.pic['goodspic'].append(form['newpic'])
                        flag_modified(newdata, "pic")
                        dbsession.commit()
                    data['data'] = json.loads(json.dumps(
                        BUSTORE.query.get(str(form['id'])), default=BUSTORE.tojson))
                except Exception as e:
                    app.logger.error(e)
            else:
                code = 418
        else:
            code = 418
    
    return jsonify(code=code, data=data, msg=msg)



@app.route('/get_bustore_data_by_site', methods=['GET'])
def get_bustore_data_by_site():
    # 初始化返回数据，规范为code/data/msg
    code = 200
    data = {
    }
    msg = ''
    method = request.method
    if method == 'GET':
        # GET方法需要判断action参数，action可以是get/handle，用于区分获取资源请求和操作请求
        argsdict = dict(request.args)
        limitselect=False
        if 'limit' in argsdict and int(argsdict['limit']) !=0 and 'offset' in argsdict :
            limitselect=True  
        if 'action' in argsdict and argsdict['action'] == 'get' and 'site' in argsdict  :
            site=json.loads(argsdict['site'])
            if 'lat' not in site or 'lng' not in site:
                code=418
            else:
                # lat 纬度，lng 经度
                bustoreList=[]
                data['data'] = json.loads(json.dumps(bustoreList, default=BUSTORE.tojson))
        else:
            code = 418
    return jsonify(code=code, data=data, msg=msg)


def calcuteLong(init_lat,init_lng,target_lat,target_lng):
    long=0
    lng1, lat1, lng2, lat2 = map(radians, [float(init_lng), float(init_lat), float(target_lng), float(target_lat)]) # 经纬度转换成弧度
    dlon=lng2-lng1
    dlat=lat2-lat1
    a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance=2*asin(sqrt(a))*6371*1000 # 地球平均半径，6371km
    long=round(distance/1000,3)
    return long