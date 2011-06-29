#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.

from util.base import *

class update_shop(handler):
    def get(self):
        shop.refresh()
        self.response.out.write('Update shop cache')

class update_items_onsale(handler):
    def get(self):
        items.refresh_onsale()
        self.response.out.write('Update product_onsale cache')

class update_items_instock(handler):
    def get(self):
        items.refresh_instock()
        self.response.out.write('Update product_instock cache')

class showcase(handler):
    def get(self):
        flag=memcache.get('cron_showcase','flag')
        if type(flag) is types.ListType and len(flag)>0:
            appkey=flag.pop(0)
            memcache.set('cron_showcase',flag,0,0,'flag')
            shop_key=filter(lambda x:x['appkey']==appkey,CONFIG['SHOP_LIST'])[0]
            client=TopClient()
            client.appkey=shop_key['appkey']
            client.secretKey=shop_key['secretKey']
            showcase=set(items.showcase(shop_key['appkey']))|set(items.instock_showcase(shop_key['appkey']))
            onsale=set([value[0] for value in items.onsale_sort(shop_key['appkey'])[:shop.info(shop_key['appkey'])['shop']['all_count']]])
            req=ItemRecommendDelete()
            for value in showcase-onsale:
                req.setNumIid(value)
                client.execute(req.getApiParas())
            req=ItemRecommendAdd()
            for value in onsale-showcase:
                req.setNumIid(value)
                client.execute(req.getApiParas())
        self.response.out.write('Refresh showcase')

class showplat(handler):
    def get(self):
        flag=memcache.get('cron_showplat','flag')
        flag_onsale=memcache.get('cron_showplat_onsale','flag')
        appkey=memcache.get('cron_showplat_appkey','flag')
        if type(flag) is types.ListType and len(flag)>0 and (type(flag_onsale) is not types.ListType or len(flag_onsale)==0 or appkey is None):
            appkey='12194338'#flag.pop(0)
            memcache.set('cron_showplat',flag,0,0,'flag')
            memcache.set('cron_showplat_onsale',items.onsale_sort(appkey),0,0,'flag')
            memcache.set('cron_showplat_appkey',appkey,0,0,'flag')
        if type(flag_onsale) is types.ListType and len(flag_onsale)>0 and appkey is not None:
            showplat=items.showplat(appkey)
            num_iid='10400309819'#flag_onsale.pop(0)[0]
            memcache.set('cron_showplat_onsale',flag_onsale,0,0,'flag')
            for value in showplat:
                self.response.out.write(num_iid)
                self.response.out.write(':')
                self.response.out.write(value['num_iid'])
                self.response.out.write('<br>')
            shop_key=filter(lambda x:x['appkey']==appkey,CONFIG['SHOP_LIST'])[0]
            client=TopClient()
            client.appkey=shop_key['appkey']
            client.secretKey=shop_key['secretKey']
            req=ItemGet()
            req.setNumIid(num_iid)
            req.setFields('desc')
            desc=client.execute(req.getApiParas())['item']['desc']
            desc='%s%s'%('test',desc)
            #re.sub(r'<img.*?src=[\'\"]?([^\'^\"^\s]+).*?>','',desc)
            req=ItemUpdate()
            req.setNumIid(num_iid)
            req.setDesc(desc)
            client.execute(req.getApiParas())
        self.response.out.write('Refresh showplat')

def main():
    application=webapp.WSGIApplication([
                                        (r'/cron/shop.*',update_shop),
                                        (r'/cron/items_onsale.*',update_items_onsale),
                                        (r'/cron/items_instock.*',update_items_instock),
                                        (r'/cron/showcase.*',showcase),
                                        (r'/cron/showplat.*',showplat),
                                        ],debug=CONFIG['DEBUG'])
    util.run_wsgi_app(application)

if __name__=='__main__':
    main()