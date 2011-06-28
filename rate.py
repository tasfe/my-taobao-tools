#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.
# 交易评价

from util.base import *

class MainHandler(handler):
    def get(self):
        self.template_values=CONFIG
        self.render('main.html')

def main():
    application=webapp.WSGIApplication([
                                        (r'/rate.*',MainHandler),
                                        ],debug=CONFIG['DEBUG'])
    util.run_wsgi_app(application)

if __name__=='__main__':
    main()