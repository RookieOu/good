#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from App import  db
from sqlalchemy.dialects.postgresql import BOOLEAN,INTEGER,VARCHAR,JSONB,ARRAY
from sqlalchemy.sql import func,text
from sqlalchemy import Column,Table
from App.util.security import getNewID



#类
class MTRANSACTION(db.Model):
    #用户表名
    __tablename__='m_transaction'
    #id，主键，采用uuid
    id=db.Column(VARCHAR,primary_key=True)
    
    # 批次编号:日期+随机码
    code=db.Column(VARCHAR)
    # 批次名称
    name=db.Column(VARCHAR)
    # 交易状态：未开始/进行中/已结束
    status=db.Column(VARCHAR)
    # 交易开始时间
    begin_date=db.Column(VARCHAR)
    # 交易计划结束时间
    plan_end_date=db.Column(VARCHAR)
    # 交易实际结束时间
    end_date=db.Column(VARCHAR)
    # 报价方式：价差模式/顺价模式
    bidding_type=db.Column(VARCHAR)
    # 出清方式：统一出清/按报价出清
    clear_type=db.Column(VARCHAR)
    # 价格撮合方式：高价出清/低价出清/平均值出清/按比例出清
    p_clear_type=db.Column(VARCHAR)
    # 价格出清比例：当价格按比例出清时有效，0-100
    p_clear_ratio=db.Column(INTEGER)
    # 是否发布:发布后不能再修改配置
    ispublic=db.Column(BOOLEAN)
    # 交易类型:集中竞价交易/滚动撮合交易/能量块联合出清交易
    tran_type=db.Column(VARCHAR)
    # 交易时段配置:
    # 1.配置划分时段，按小时划分。例如4段：（00:00-4:00,4:00-8:00,8:00-18:00,18:00-24:00）；
    # 2.配置各时段可申报电量的段数，影响申报时的界面
    # 3.配置各时段的总供给电量与需求电量
    # 4.配置各时段的申报量约束，可按总电量占比进行约束
    # 5.配置各时段的上网电价、输配电价、政府基金及附加、以及目录电价
    # 6.配置各时段的申报价格约束，包括最低与最高限价
    trun_interval=db.Column(JSONB)


    # 市场主体相关
    # 售电公司数量
    m_sale_cp_num=db.Column(INTEGER)
    # 电力用户数量
    m_ele_user_num=db.Column(INTEGER)
    # 发电企业数量
    m_pro_cp_num=db.Column(INTEGER)
    # 市场主体捣乱机器人
    # 角色：售电公司/电力用户/发电企业
    # 数量
    # 策略：激进、保守、随机
    m_robot=db.Column(JSONB)

    # 市场主体补缺机器人
    # 角色：售电公司/电力用户/发电企业
    # 数量
    # 策略：激进、保守、随机
    m_sup_robot=db.Column(JSONB)
    # 市场实际主体
    # 售电公司
    m_sale_cp_real=db.Column(ARRAY(VARCHAR))
    # 电力用户
    m_ele_user_real=db.Column(ARRAY(VARCHAR))
    # 发电企业
    m_pro_cp_real=db.Column(ARRAY(VARCHAR))


    # 交易结果
    m_result=db.Column(JSONB)

    # 平台相关
    # 创建人
    create_user=db.Column(VARCHAR)
    create_userid=db.Column(VARCHAR)
    # 创建时间
    create_date=db.Column(VARCHAR)
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
                    'code':item.code,
                    'name':item.name,
                    'status':item.status,
                    'begin_date':item.begin_date,
                    'plan_end_date':item.plan_end_date,
                    'end_date':item.end_date,
                    'bidding_type':item.bidding_type,
                    'clear_type':item.clear_type,
                    'ispublic':item.ispublic,
                    'tran_type':item.tran_type,
                    'trun_interval':item.trun_interval,
                    'm_sale_cp_num':item.m_sale_cp_num,
                    'm_ele_user_num':item.m_ele_user_num,
                    'm_pro_cp_num':item.m_pro_cp_num,
                    'm_robot':item.m_robot,
                    'm_sale_cp_real': [x for x in item.m_sale_cp_real],
                    'm_ele_user_real': [x for x in item.m_ele_user_real],
                    'm_pro_cp_real': [x for x in item.m_pro_cp_real],
                    'm_result':item.m_result,
                    'isdelete':item.isdelete,
                    'create_user':item.create_user,
                    'create_date':item.create_date,
                    'm_sup_robot':item.m_sup_robot,
                    'create_userid':item.create_userid,
                    'p_clear_type':item.p_clear_type,
                    'p_clear_ratio':item.p_clear_ratio

                })
            return jsondata
        else:
            return {
                'id':data.id,
                'code':data.code,
                'name':data.name,
                'status':data.status,
                'begin_date':data.begin_date,
                'plan_end_date':data.plan_end_date,
                'end_date':data.end_date,
                'bidding_type':data.bidding_type,
                'clear_type':data.clear_type,
                'ispublic':data.ispublic,
                'tran_type':data.tran_type,
                'trun_interval':data.trun_interval,
                'm_sale_cp_num':data.m_sale_cp_num,
                'm_ele_user_num':data.m_ele_user_num,
                'm_pro_cp_num':data.m_pro_cp_num,
                'm_robot':data.m_robot,
                'm_sale_cp_real': [x for x in data.m_sale_cp_real],
                'm_ele_user_real': [x for x in data.m_ele_user_real],
                'm_pro_cp_real': [x for x in data.m_pro_cp_real],
                'm_result':data.m_result,
                'isdelete':data.isdelete,
                'create_user':data.create_user,
                'create_date':data.create_date,
                'm_sup_robot':data.m_sup_robot,
                'create_userid':data.create_userid,
                'p_clear_type':data.p_clear_type,
                'p_clear_ratio':data.p_clear_ratio
                }



# from flask import json    
def listdata():
    db.create_all()

    


