#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  App import dbsession,  app
import asyncio,datetime
from flask import json, jsonify, g, request
from  App.model.m_transaction import MTRANSACTION
from  App.util.security import getNewID,MD5
from sqlalchemy import case,func,desc
import copy,decimal
from sqlalchemy.orm.attributes import flag_modified


@app.route('/get_m_transaction_data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_m_transaction_data():
    # 初始化返回数据，规范为code/data/msg
    code = 200
    data = {
    }
    msg = ''
    method = request.method
    if method == 'GET':
        # GET方法需要判断action参数，action可以是get/handle，用于区分获取资源请求和操作请求
        argsdict=request.args.to_dict()
        # argsdict['iscount']=True
        # argsdict['offset']=0
        # argsdict['limit']=10
        # argsdict['orderby']={'staffcode':'asc'}
        # argsdict['filterby']={'staffcode':'200'}
        if 'action' in argsdict and argsdict['action'] == 'get':
            # 是否查总行数iscount，是否查询起点offset，是否查询行数limit，排序orderby,过滤filterby
            if 'offset' in argsdict and 'limit' in argsdict and 'orderby' in argsdict and 'filterby' in argsdict :
                q = dbsession.query(MTRANSACTION).filter(MTRANSACTION.isdelete==False)
                c=dbsession.query(func.count(MTRANSACTION.id)).filter(MTRANSACTION.isdelete==False)
                if json.loads(argsdict['filterby'])!={}:
                    for attr, value in json.loads(argsdict['filterby']).items():
                        if(attr=='ispublic'):
                            q = q.filter(getattr(MTRANSACTION, attr)==value)
                            c = c.filter(getattr(MTRANSACTION, attr)==value)
                        else:
                            q = q.filter(getattr(MTRANSACTION, attr).like("%%%s%%" % value))
                            c = c.filter(getattr(MTRANSACTION, attr).like("%%%s%%" % value))
                if json.loads(argsdict['orderby'])!={}:
                    for attr, value in json.loads(argsdict['orderby']).items():
                        if value=='asc':
                            q = q.order_by(attr)
                        else:
                            q = q.order_by(desc(attr))
                else:
                    q=q.order_by(desc('code'))
                if int(argsdict['limit'])!=-1:
                    q=q.limit(argsdict['limit'])
                q=q.offset(int(argsdict['offset']))
                if 'iscount' in argsdict and argsdict['iscount'] == 'true':
                    a=c.all()
                    data['countall']=a[0][0]
                data['data'] = json.loads(json.dumps(q.all(), default=MTRANSACTION.tojson))
            elif 'id' in argsdict and argsdict['id']!='':
                data['data'] = json.loads(json.dumps(dbsession.query(
                    MTRANSACTION).filter(MTRANSACTION.id==str(argsdict['id'])).all(), default=MTRANSACTION.tojson))
            else:
                data['data'] = json.loads(json.dumps(dbsession.query(
                    MTRANSACTION).all(), default=MTRANSACTION.tojson))
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
            # 按时间自动创建编号
            nowdate= datetime.datetime.now()
            try:
                newdata = MTRANSACTION(id=id, code=nowdate.strftime('%Y%m%d%H%M%S%f'), name=form['name'],
                    status=form['status'],begin_date=form['begin_date'],plan_end_date=form['plan_end_date'],
                    end_date=form['end_date'],bidding_type=form['bidding_type'],clear_type=form['clear_type'],
                    ispublic=form['ispublic'],tran_type=form['tran_type'],trun_interval=form['trun_interval'],
                    m_sale_cp_num=form['m_sale_cp_num'],m_ele_user_num=form['m_ele_user_num'],m_pro_cp_num=form['m_pro_cp_num'],
                    m_robot=form['m_robot'],m_sup_robot=form['m_sup_robot'],m_sale_cp_real=form['m_sale_cp_real'],
                    m_ele_user_real=form['m_ele_user_real'],m_pro_cp_real=form['m_pro_cp_real'],
                    p_clear_type=form['p_clear_type'],p_clear_ratio=form['p_clear_ratio'],
                    m_result=form['m_result'],create_user=g.user.realname,create_userid=str(g.user.id),create_date=nowdate.strftime('%Y-%m-%d %H:%M:%S'),
                    isdelete=False)
                dbsession.add(newdata)
                dbsession.commit()
                data['data'] = json.loads(json.dumps(
                    MTRANSACTION.query.get(str(id)), default=MTRANSACTION.tojson))
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
                newdata = MTRANSACTION.query.get(str(form['id']))
                ori_status=newdata.status
                newdata.name = form['name']
                newdata.status = form['status']
                newdata.begin_date = form['begin_date']
                newdata.plan_end_date = form['plan_end_date']
                newdata.end_date = form['end_date']
                newdata.bidding_type = form['bidding_type']
                newdata.clear_type = form['clear_type']
                newdata.ispublic = form['ispublic']
                newdata.tran_type = form['tran_type']
                newdata.trun_interval = form['trun_interval']
                newdata.m_sale_cp_num = form['m_sale_cp_num']
                newdata.m_ele_user_num = form['m_ele_user_num']
                newdata.m_pro_cp_num = form['m_pro_cp_num']
                newdata.m_robot = form['m_robot']
                newdata.m_sup_robot = form['m_sup_robot']
                newdata.m_sale_cp_real = form['m_sale_cp_real']
                newdata.m_ele_user_real = form['m_ele_user_real']
                newdata.m_pro_cp_real = form['m_pro_cp_real']
                newdata.m_result = form['m_result']
                newdata.p_clear_ratio=form['p_clear_ratio']
                newdata.p_clear_type=form['p_clear_type']
                # flag_modified(newdata,'m_result')

                dbsession.commit()
                
                data['data'] = json.loads(json.dumps(
                    MTRANSACTION.query.get(str(form['id'])), default=MTRANSACTION.tojson))
            except Exception as e:
                # 生产上可以改为log
                print(e)
        else:
            code = 418
    elif method == 'DELETE':
        # 删除资源
        argsdict=request.args.to_dict()
        if 'id' in argsdict:
            deldata = MTRANSACTION.query.get(str(argsdict['id']))
            deldata.isdelete=True
            # dbsession.delete(deldata)
            dbsession.commit()
            data['data'] = json.loads(json.dumps(deldata, default=MTRANSACTION.tojson))
        else:
            code = 418
    return jsonify(code=code, data=data, msg=msg)

# 具体操作

# 以时段为单位获取

def builddata():
    datalist=dbsession.query(MTRANSACTION).filter(MTRANSACTION.isdelete==False).filter(MTRANSACTION.status=='已结束').all()
    
            
    dbsession.commit()
def objtostr(data):
    if isinstance(data,list):
        tmplist=[]
        for d in data:
            tmplist.append(objtostr(d))
        return tmplist
    elif isinstance(data,dict):
        tmpdict={}
        for d in list(data.keys()):
            tmpdict[d]=objtostr(data[d])
        return tmpdict
    elif isinstance(data,decimal.Decimal):
        return str(data)
    else:
        return data
