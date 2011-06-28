#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.

from util.base import *

class MainHandler(handler):
    def get(self):
        self.template_values=CONFIG
        self.render('main.html')

class HtmlHandler(handler):
    def get(self):
        if self.request.get('file'):
            self.template_values=CONFIG
            self.render("%s.html"%(self.request.get('file')))

class TestHandler(handler):
    def get(self):
        print ''
        print items.showplat()

def main():
    application=webapp.WSGIApplication([
                                        (r'/*',MainHandler),
                                        (r'/html',HtmlHandler),
                                        (r'/test',TestHandler),
                                        ],debug=CONFIG['DEBUG'])
    util.run_wsgi_app(application)

if __name__=='__main__':
    main()