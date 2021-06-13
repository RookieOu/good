#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#表单验证csrf加密配置
CSRF_ENABLED=True
#会话密钥
SECRET_KEY='A0Zr98j/0R~jejdke!muesdKYd],/?eRT'
#PostgreSQL数据库连接配置
SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://goodmanage_adm:password@106.13.26.23:5432/goodmanage0530?client_encoding=utf8'
#数据库连接池大小
SQLALCHEMY_POOL_SIZE=20
#数据库连接超时时间
SQLALCHEMY_POOL_TIMEOUT=None
#数据库连接回收时间
SQLALCHEMY_POOL_RECYCLE=3600
SQLALCHEMY_TRACK_MODIFICATIONS=True
#上传文件所在文件夹
UPLOAD_FOLDER='uploadfiles'
#上传文件最大10M
MAX_CONTENT_LENGTH = 10 * 1024 * 1024
#应用后端部署IP或域名,在上传文件后返回文件路径用
SERVER_ADDR="https://127.0.0.1:5000"
APPID=''
# 小程序会话保持时长
WX_SESSION_OVERTIME=1440
# 小程序
# 开发者秘钥
DEVELOP_KEY=''
# 小程序id
WX_APPID=''
# 小程序秘钥
WX_APPSECRET=''
# 商户号
MCH_ID=''
# 商户秘钥
MCH_KEY=''
# 支付成功后通知url
WX_PAY_NOTIFY_URL='https://test.com.cn/wx_pay_result'
