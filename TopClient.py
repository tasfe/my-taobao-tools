#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.
import sys,urllib,urllib2,types,time,simplejson,md5
from TopApi import *

class TopClient(object):

    def __init__(self):
        self.appkey=''
        self.secretKey=''
        self.gatewayUrl='http://gw.api.taobao.com/router/rest'
        self.format='json'
        self.signMethod='md5'
        self.apiVersion='2.0'

    def generateSign(self,args):
        #生成签名
        for k,v in args.iteritems():
            if type(args[k]) is types.UnicodeType:
                args[k]=v.encode('UTF-8')
        return md5.new(self.secretKey+''.join(['%s%s'%(k,v) for k,v in sorted(args.items())])+self.secretKey).hexdigest().upper()

    def execute(self,args):
        try:
            sysParams={
                'app_key':self.appkey,
                'format':self.format,
                'sign_method':self.signMethod,
                'timestamp':time.strftime('%Y-%m-%d %X',time.localtime()),
                'v':self.apiVersion
            }
            #组装参数
            sysParams.update(args)
            sysParams['sign']=self.generateSign(sysParams)
            #发送查询
            response=urllib2.urlopen(urllib2.Request(self.gatewayUrl,urllib.urlencode(sysParams))).read()
            #返回处理
            response=simplejson.loads(response.decode('UTF-8'),strict=False)
            if response.has_key('error_response'):
                sys.exit("Error%s: %s"%(response['error_response']['code'],response['error_response']['msg']))
            else:
                response=response.values().pop()
            return response
        except:
            #异常处理
            time.sleep(5)
            return self.execute(args)
            

if __name__=='__main__':
    pass