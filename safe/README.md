# 需要补充信息
./start.py  
|——需要配置生产发布的端口、证书

./config.py
|——需要配置SECRET_KEY、SQLALCHEMY_DATABASE_URI、SERVER_ADDR、WX_PAY_NOTIFY_URL、微信小程序APP_ID等

./gunicorn.conf
|——需要配置bind、日志路径名称、证书


