#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.

import os,math,types,time,simplejson,re
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api.memcache import Client
from TopClient import *
memcache=Client()

CONFIG={
    'DEBUG':True,
    'SYSTEM_NAME':u'淘宝店铺自动助理',
    'SYSTEM_VER':u'11.7',
    'SYSTEM_USER':users.get_current_user(),
    'SHOP_LIST':({'appkey':'111','secretKey':'222'},{'appkey':'111','secretKey':'222'})
}
if __name__=='__main__':
    pass