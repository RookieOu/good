#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import redirect,  request, session, g, url_for, jsonify, json, make_response
from  App import dbsession, lm,  app
# from  App.model.base_user import BASEUSER
from  App.model.buuser import BUUSER
from flask_login import current_user, login_required, logout_user, login_user
from urllib.request import urlopen
from  App.util.security import getHMACStr, getEsbHeaderValue,MD5
from  App.util.security import getNewID,sessionDecode,sessionEncode
import http.client
import urllib.parse
#小程序接口调用路径需加入到此列表
accessWithoutTokenPath = ['/c_login', '/', '/index','/getfiles','/get_bugoods_by_typeid']
# 登陆认证，结合公司统一认证


@app.route('/c_login', methods=['GET', 'POST'])
def c_login():
    # 初始化返回数据，规范为code/data/msg
    code = 200
    data = {
        'token': '',
    }
    msg = ''
    header = dict(request.headers)
    
    # 管理平台端
    # 如果用户已登录，直接返回session中token
    if g.user is not None and g.user.is_authenticated:
        data['token'] = g.user.staffcode
        return jsonify(code=code, data=data, msg=msg)
    # 如果用户未登录，获取提交的用户名和密码
    argsdict = json.loads(str(request.data, encoding='utf-8'))
    userName = ''
    password = ''
    if 'userName' in argsdict and 'password' in argsdict:
        # 工号密码登录
        userName = argsdict['userName']
        password = argsdict['password']
    elif 'userName' in argsdict and 'password' in argsdict:
        # 手机密码登录######################################
        userName = argsdict['userName']
        password = argsdict['password']
    elif 'userName' in argsdict and 'password' in argsdict:
        # 邮箱密码登录########################################
        userName = argsdict['userName']
        password = argsdict['password']
    if userName!='' and password !='':
        
        
        # 平台权限判断
        user = BUUSER.query.filter_by(staffcode=userName).first()
        if user is not None:
            
            if user.pw==MD5(password) :
                logout_user()
                login_user(user)
                data['token'] = g.user.staffcode
                return jsonify(code=code, data=data, msg=msg)
            else:
                code = 508
                msg = '密码错误'
                return jsonify(code=code, data=data, msg=msg)
        else:
            code = 508
            msg = '您不在平台操作员名单内，请联系平台负责人，tel:9233'
            return jsonify(code=code, data=data, msg=msg)
        
    else:
        code = 508
        msg = '用户名/密码不能为空'
        return jsonify(code=code, data=data, msg=msg)

# 加载登录用户信息


@lm.user_loader
def load_user(id):
    user=BUUSER.query.filter_by(id=id).first()
    # if user is None:
    #     user=BASEUSER.query.filter_by(id=id).first()
    return user

# 登录前操作：将当前用户加入到flask上下文中作为可全局调用对象
# 验证后端登录状态，通过token获取，token即工号
# 508：服务端未登录
# 408：未传入token验证登录
# 418：传入参数缺失

@lm.request_loader
def load_request(request):
    # if 'Sessiontoken' in request.headers and request.headers['Sessiontoken']!='':
    argsdict = dict(request.headers)
    if 'Sessiontoken' in argsdict:
        user_id=sessionDecode(request.headers['Sessiontoken'],app.config['WX_SESSION_OVERTIME']) 
        if user_id !=False:
            session['user_id']=user_id
            user=BUUSER.query.get(str(user_id))
            return user
        else:
            session['user_id']=request.headers['Sessiontoken']
            user=BUUSER.query.filter(BUUSER.staffcode==str(session['user_id'])).first()
            return user
    else:
        return None

@app.before_request
def before_request():
    # request.cookies={'sess'}
    g.user = current_user
    code = 200
    msg = ''
    data = {}
    if request.path in accessWithoutTokenPath or '/static' in request.path:
        pass
    else:
        # 管理平台后端认证
        if 'staffcode' in dir(g.user) :
            pass
        else:
            code = 508
            msg='未登录'
            return jsonify(code=code, data=data, msg=msg)
        
# 注销登录


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
   
    code = 200
    data = {}
    msg = ''
    return jsonify(code=code, data=data, msg=msg)


@app.after_request
def af_request(resp):
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp = make_response(resp)
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    if 'HTTP_ORIGIN' in request.environ:
        resp.headers['Access-Control-Allow-Origin'] = request.environ['HTTP_ORIGIN']
    else:
        resp.headers['Access-Control-Allow-Origin'] = '*'
    if "location" in dict(request.args):
        resp.headers["location"]=dict(request.args)["location"]
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTION'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,X-URL-PATH,Sessiontoken'
    return resp
