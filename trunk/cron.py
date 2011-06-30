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
        shop_key=base.flag()['showcase']
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
        shop_key=memcache.get('cron_showplat_key','flag')
        flag_onsale=memcache.get('cron_showplat_onsale','flag')
        if type(flag_onsale) is not types.ListType or len(flag_onsale)==0 or type(shop_key) is not types.DictType:
            shop_key=base.flag()['showplat']
            flag_onsale=items.onsale_sort(shop_key['appkey'])
            memcache.set('cron_showplat_key',shop_key,0,0,'flag')
            memcache.set('cron_showplat_onsale',flag_onsale,0,0,'flag')
        if type(flag_onsale) is types.ListType or len(flag_onsale)>0 or type(shop_key) is types.DictType:
            num_iid=flag_onsale.pop(0)[0]
            memcache.set('cron_showplat_onsale',flag_onsale,0,0,'flag')
            client=TopClient()
            client.appkey=shop_key['appkey']
            client.secretKey=shop_key['secretKey']
            req=ItemGet()
            req.setNumIid(num_iid)
            req.setFields('cid,desc')
            item=client.execute(req.getApiParas())['item']
            showplat=items.showplat(shop_key['appkey'],item['cid'])
            adstr=u'<a name="eshop_begin_cid%s"></a><div style="width:750px;font-size:14px;margin:0px auto;overflow:hidden;background-color:#ffffff;"><img src="http://eshop.alibaba.com/qbuilder/STATIC_SERVER/c2c/face0/images/goodspromotion/templete2.jpg" style="float:left;" /><ul style="width:726px;margin:0px;padding:0px 12px;overflow:hidden;float:left;">'%(item['cid'],)
            for value in showplat:
                adstr='%s%s'%(adstr,u'<li style="width:222px;padding:0px 10px;overflow:hidden;display:inline;float:left;" title="点击查看详情"><a href="http://item.taobao.com/item.htm?id=%s" style="color:#aaaaaa;" target="_blank"><img src="%s_310x310.jpg" style="width:220px;height:220px;border:#cccccc 1px solid;float:left;" /></a><p style="width:222px;padding:5px 0px;overflow:hidden;float:left;"><a href="http://item.taobao.com/item.htm?id=%s" style="width:222px;color:#aaaaaa;overflow:hidden;float:left;" target="_blank">%s</a><b style="width:102px;overflow:hidden;color:#be2600;font-size:20px;font-weight:bold;float:right;"><span style="color:#aaaaaa;">&yen;&nbsp;</span>%s</b></p></li>'%(value['num_iid'],value['pic_url'],value['num_iid'],value['title'],value['price']))
            adstr='%s%s'%(adstr,u'</ul><img src="http://eshop.alibaba.com/qbuilder/STATIC_SERVER/c2c/face0/images/goodspromotion/templeteft2.jpg" style="float:left;" /></div><a name="eshop_end_cid%s"></a>'%(item['cid'],))
            item['desc']=re.sub(r'<a.*?name=[\'\"]?(eshop_begin_).*?>.*?</a>[\s\S]*?<a.*?name=[\'\"]?(eshop_end_).*?>.*?</a>','',item['desc'])
            item['desc']='%s%s'%(adstr,item['desc'])
            req=ItemUpdate()
            req.setNumIid(num_iid)
            req.setDesc(item['desc'])
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