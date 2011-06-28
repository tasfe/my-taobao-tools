#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.

from util.base import *

class userlist(handler):
    def get(self):
        data={}
        for value in CONFIG['SHOP_LIST']:
            info=shop.info(value['appkey'])
            data[value['appkey']]={'user':info['user']['nick'],'shop':info['shop']['title']}
        self.response.out.write(simplejson.dumps(data))

class userchange(handler):
    def get(self):
        try:
            base.change(self.request.get('appkey'))
            self.response.out.write('success')
        except:
            self.response.out.write('failure')

class findimg(handler):
    def get(self):
        try:
            result=urlfetch.fetch(self.request.get('url'))
            if result.status_code==200:
                request=re.findall(r'<img.*?src=[\'\"]?([^\'^\"^\s]+).*?>',result.content)
                if len(request)>0:
                    self.response.out.write(simplejson.dumps(request))
                else:
                    self.response.out.write('["failure"]')
            else:
                self.response.out.write('["failure"]')
        except:
            self.response.out.write('["failure"]')

def main():
    application=webapp.WSGIApplication([
                                        (r'/ajax/userlist.*',userlist),
                                        (r'/ajax/userchange.*',userchange),
                                        (r'/ajax/findimg.*',findimg),
                                        ],debug=CONFIG['DEBUG'])
    util.run_wsgi_app(application)

if __name__=='__main__':
    main()