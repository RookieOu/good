# -*- coding: utf-8 -*-
import os
import uuid
import platform
from flask import json, jsonify, g, request,send_from_directory
from  App import dbsession,  app
from werkzeug.utils import secure_filename

if platform.system() == "Windows":
    slash = '\\'
else:
    platform.system()=="Linux"
    slash = '/'
UPLOAD_FOLDER = app.config['UPLOAD_FOLDER']
ALLOW_EXTENSIONS = set(['jpg', 'png', 'jpeg'])
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 判断文件后缀是否在列表中
def allowed_file(filename):
    return '.' in filename and  filename.rsplit('.', 1)[1].lower() in ALLOW_EXTENSIONS

@app.route('/get_uploadfile_data',methods=['GET','POST'])
def upload_file():
    # 初始化返回数据，规范为code/data/msg
    code = 200
    data = {
    }
    msg = ''
    if request.method =='POST':
        #判断文件夹是否存在，如果不存在则创建
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        else:
            pass
        #获取post过来的文件名称，从name=file参数中获取
        file = request.files['file']

        if file and (allowed_file(file.filename) or file.content_type=='image/png'):
            # secure_filename方法会去掉文件名中的中文
            filename = secure_filename(file.filename)
            if filename=='blob':
                filename='blob.png'
            #因为上次的文件可能有重名，因此使用uuid保存文件
            new_file_name=''
            if len(filename.rsplit('.', 1))==1:
                new_file_name = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[0]
            else:
                new_file_name = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1]
            try:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],new_file_name))
                # base_path = os.getcwd()
                # file_path = base_path + slash + app.config['UPLOAD_FOLDER'] + slash + new_file_name
                data['data'] = {
                    'name':new_file_name,
                    'url':app.config['SERVER_ADDR']+'/getfiles?id='+new_file_name,
                    'percentage': 100,
                    'status': "finished"
                }
            except Exception as e:
                print(e)
                code=500
        else:
            code = 418
            msg="文件格式有误！"
    return jsonify(code=code, data=data, msg=msg)


@app.route('/getfiles',methods=['GET'])
def getfiles():
    #测试用，后期通过nginx直接分发
    if request.method == 'GET':
        argsdict=request.args.to_dict()
        if 'id' in argsdict:
            base_path = os.getcwd()
            id=argsdict['id'].split('/')[-1]
            file_map_list=[
                {
                    "id":"1c124677-32cc-43fd-8a87-7eb722e9d9ea",
                    "url":"a/a.txt"
                },
                {
                    "id":"2c124677-32cc-43fd-8a87-7eb722e9d98a",
                    "url":"b.txt"
                },
            ]
            target_file=[x["url"] for x in file_map_list if x["id"]==id]
            if len(target_file)>0:
                id=target_file[0]
            # else:
            #     return 'None'
            try:
                return send_from_directory(base_path + slash + app.config['UPLOAD_FOLDER'] + slash , id)
                # return send_from_directory(base_path + slash + app.config['UPLOAD_FOLDER'] + slash , argsdict['id'])
            except Exception as e:
                return 'None'
    return 'None'

@app.route('/removefiles',methods=['DELETE'])
def removefile():
    code = 200
    data = {
    }
    msg = ''
    if request.method == 'DELETE':
        argsdict=request.args.to_dict()
        if 'id' in argsdict:
            base_path = os.getcwd()
            try:
                fileload=base_path + slash + app.config['UPLOAD_FOLDER'] + slash +argsdict['id']
                if os.path.exists(fileload):
                    os.remove(fileload)
                else:
                    code=418
                    msg='文件不存在！'
                # return send_from_directory(base_path + slash + app.config['UPLOAD_FOLDER'] + slash , argsdict['name'])
            except Exception as e:
                print(e)
                code=418
                msg='文件删除失败'
        else:
            code=418
    else:
        code=418
    return jsonify(code=code, data=data, msg=msg)


def removeAva(initid):
    code = 200
    msg=''
    base_path = os.getcwd()
    ids=initid.split('=')
    if len(ids)>1:
        id=ids[1]
        try:
            fileload=base_path + slash + app.config['UPLOAD_FOLDER'] + slash +id
            if os.path.exists(fileload):
                os.remove(fileload)
            else:
                code=418
                msg='文件不存在！'
            # return send_from_directory(base_path + slash + app.config['UPLOAD_FOLDER'] + slash , argsdict['name'])
        except Exception as e:
            print(e)
            code=418
            msg='文件删除失败'
       
    return code,msg