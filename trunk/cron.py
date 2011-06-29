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
            appkey=flag.pop(0)
            memcache.set('cron_showplat',flag,0,0,'flag')
            memcache.set('cron_showplat_onsale',items.onsale_sort(appkey),0,0,'flag')
            memcache.set('cron_showplat_appkey',appkey,0,0,'flag')
        if type(flag_onsale) is types.ListType and len(flag_onsale)>0 and appkey is not None:
            showplat=items.showplat(appkey)
            num_iid=flag_onsale.pop(0)[0]
            memcache.set('cron_showplat_onsale',flag_onsale,0,0,'flag')
            adstr=u'<a name="eshop_begin_wsb19830310"></a><div style="width:750px;font-size:14px;margin:0px auto;overflow:hidden;background-color:#ffffff;"><img src="http://eshop.alibaba.com/qbuilder/STATIC_SERVER/c2c/face0/images/goodspromotion/templete2.jpg" style="float:left;" /><ul style="width:726px;margin:0px;padding:0px 12px;overflow:hidden;float:left;">'
            for value in showplat:
                adstr='%s%s'%(adstr,u'<li style="width:222px;padding:0px 10px;display:inline;float:left;" title="点击查看详情"><a href="http://item.taobao.com/item.htm?id=%s" style="color:#aaaaaa;" target="_blank"><img src="%s_310x310.jpg" style="width:220px;height:220px;border:#cccccc 1px solid;" /></a><p style="line-height:20px;cursor:pointer;"><a href="http://item.taobao.com/item.htm?id=%s" style="color:#aaaaaa;float:left;" target="_blank">%s</a><b style="color:#be2600;font-size:20px;font-weight:bold;float:right;"><span style="color:#aaaaaa;font-size:14px;font-weight:normal;">￥</span>%s</b></p></li>'%(value['num_iid'],value['pic_url'],value['num_iid'],value['title'],value['price']))
            adstr='%s%s'%(adstr,u'</ul><img src="http://eshop.alibaba.com/qbuilder/STATIC_SERVER/c2c/face0/images/goodspromotion/templeteft2.jpg" style="float:left;" /></div><a name="eshop_end_wsb19830310"></a>')
            shop_key=filter(lambda x:x['appkey']==appkey,CONFIG['SHOP_LIST'])[0]
            client=TopClient()
            client.appkey=shop_key['appkey']
            client.secretKey=shop_key['secretKey']
            req=ItemGet()
            req.setNumIid(num_iid)
            req.setFields('desc')
            desc=client.execute(req.getApiParas())['item']['desc']
            desc=re.sub(r'<a.*?name=[\'\"]?(eshop_begin_).*?>.*?</a>[\s\S]*?<a.*?name=[\'\"]?(eshop_end_).*?>.*?</a>','',desc)
            desc='%s%s'%(adstr,desc)
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