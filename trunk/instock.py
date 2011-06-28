#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.
# 库存商品

from util.base import *

class RegularHandler(handler):
    def get(self):
        instock=items.instock_shelved()
        instock_regular=items.instock_regular()
        page=self.request.get('page').isdigit() and int(self.request.get('page')) or 1
        rows=self.request.get('rows').isdigit() and int(self.request.get('rows')) or 20
        datagrid=[instock[value[0]] for value in instock_regular[(page-1)*rows:page*rows]]
        self.response.out.write(simplejson.dumps({'total':len(instock_regular),'rows':datagrid}))

class ViolationHandler(handler):
    def get(self):
        instock_violation=sorted(items.instock_violation().iteritems(),key=lambda x:x[1],reverse=False)
        page=self.request.get('page').isdigit() and int(self.request.get('page')) or 1
        rows=self.request.get('rows').isdigit() and int(self.request.get('rows')) or 20
        datagrid=[value[1] for value in instock_violation[(page-1)*rows:page*rows]]
        self.response.out.write(simplejson.dumps({'total':len(instock_violation),'rows':datagrid}))

class ShelvedHandler(handler):
    def get(self):
        instock_shelved=sorted(items.instock_shelved().iteritems(),key=lambda x:x[1],reverse=False)
        page=self.request.get('page').isdigit() and int(self.request.get('page')) or 1
        rows=self.request.get('rows').isdigit() and int(self.request.get('rows')) or 20
        datagrid=[value[1] for value in instock_shelved[(page-1)*rows:page*rows]]
        self.response.out.write(simplejson.dumps({'total':len(instock_shelved),'rows':datagrid}))

def main():
    application=webapp.WSGIApplication([
                                        (r'/instock/regular.*',RegularHandler),
                                        (r'/instock/violation.*',ViolationHandler),
                                        (r'/instock/shelved.*',ShelvedHandler),
                                        ],debug=CONFIG['DEBUG'])
    util.run_wsgi_app(application)

if __name__=='__main__':
    main()