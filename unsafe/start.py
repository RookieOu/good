#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from App import app
from gevent.pywsgi import WSGIServer
from gevent import monkey
# monkey.patch_all()
if __name__=='__main__':
    app.run(debug=True,port=5001)#本地调试