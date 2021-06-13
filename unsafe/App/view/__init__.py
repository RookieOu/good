#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from App import dbsession,app
from App.util.security import getNewPw
from flask_login import login_required
from .login import load_user
import asyncio
from App.model.base_role import BASEROLES
from flask import json,jsonify,g,render_template,request
from .privs import *
from .roles import *
from .users import *
from .sysconfig import *
from .a1001 import *
from .base_release_log import *
#openAPI
#业务视图
from .buuser import*
from .uploadfile import*

from .m_transaction import *
from .bugoods import *
from .bugoodstype import *
from .bustore import *
from .bustoretype import *


#平台主页,直接返回单页应用
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



#获取用户信息：用户信息/角色信息/权限信息
@app.route('/get_userinfo',methods=['GET','POST'])
def getUserInfo():
    #初始化返回参数
    code=200
    msg=''
    data={
        'id':'',
        'realname':'',
        'staffcode':'',
        'roles':[],
        'access':[],
        'avator':''
    }

    data['id']=g.user.id
    data['staffcode']=g.user.staffcode
    data['realname']=g.user.realname
    data['roles']=g.user.roles
    data['avator']=g.user.ava
    allprivs=[]
    roledatas=json.loads(json.dumps(dbsession.query(
                BASEROLES).all(), default=BASEROLES.tojson))
    for role in g.user.roles:
        privs=list(filter(lambda x:x['id']==role,roledatas))
        if privs!=[]:
            allprivs=allprivs+privs[0]['privs']
    data['access']=list(set(allprivs))

    return jsonify(code=code,data=data,msg=msg)
        

@app.route('/get_newpw', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_newpw(): 
    code = 200
    data = {
    }
    data['data'] = getNewPw()
    msg = ''
    return jsonify(code=code, data=data, msg=msg)

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class InputForm(FlaskForm):
    string=StringField()
    sub=SubmitField('submit')
     
@app.route('/userform',methods=['GET', 'POST'])    
def fontPage():
    info=InputForm()
    if request.method=='POST':
        string=request.form['string']
        return render_template('show.html',string=string)
    return render_template('form.html',info=info)
    