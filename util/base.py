#!/usr/bin/env python
# coding:utf-8
# Copyright 2011 WSB Inc.

import sys
sys.path.append('..')
from config import *


class handler(webapp.RequestHandler):

    def render(self,template_file):
        self.response.out.write(self.get_render(template_file))

    def get_render(self,template_file):
        try:
            template_file="template/%s"%(template_file)
            path=os.path.join(os.path.dirname(__file__),r'../',template_file)
            return template.render(path,self.template_values)
        except:
            return 'failure'


class base():

    @classmethod
    def user(self):
        CONFIG['SHOP_USER']=memcache.get('appkey')
        if type(CONFIG['SHOP_USER']) is types.StringType and len(CONFIG['SHOP_USER'])>0:
            return CONFIG['SHOP_USER']
        else:
            memcache.set('appkey',CONFIG['SHOP_LIST'][0]['appkey'])
            return self.user()

    @classmethod
    def flag(self):
        shop_key={}
        flag=memcache.get('cron_showcase','flag')
        if type(flag) is not types.ListType or len(flag)==0:
            flag=list(CONFIG['SHOP_LIST'])
        shop_key['showcase']=flag.pop(0)
        memcache.set('cron_showcase',flag,0,0,'flag')
        flag=memcache.get('cron_showplat','flag')
        if type(flag) is not types.ListType or len(flag)==0:
            flag=list(CONFIG['SHOP_LIST'])
        shop_key['showplat']=flag.pop(0)
        memcache.set('cron_showplat',flag,0,0,'flag')
        flag=memcache.get('refresh_onsale','flag')
        if type(flag) is not types.ListType or len(flag)==0:
            flag=list(CONFIG['SHOP_LIST'])
        shop_key['onsale']=flag.pop(0)
        memcache.set('refresh_onsale',flag,0,0,'flag')
        flag=memcache.get('refresh_instock','flag')
        if type(flag) is not types.ListType or len(flag)==0:
            flag=list(CONFIG['SHOP_LIST'])
        shop_key['instock']=flag.pop(0)
        memcache.set('refresh_instock',flag,0,0,'flag')
        return shop_key

    @classmethod
    def getkey(self,appkey):
        return filter(lambda x:x['appkey']==appkey,CONFIG['SHOP_LIST'])[0]

    @classmethod
    def change(self,appkey):
        memcache.set('appkey',filter(lambda x:x['appkey']==appkey,CONFIG['SHOP_LIST'])[0]['appkey'])
        self.user()


class shop(base):

    @classmethod
    def info(self,user=''):
        user=user or base.user()
        data=memcache.get('info',user)
        if type(data) is types.DictType:
            return data
        else:
            self.refresh()
            return self.info(user)

    @classmethod
    def refresh(self):
        for shop_key in CONFIG['SHOP_LIST']:
            self.request(shop_key)

    @classmethod
    def request(self,shop_key):
        client=TopClient()
        client.appkey=shop_key['appkey']
        client.secretKey=shop_key['secretKey']
        info={}
        req=UserGet()
        req.setFields('user_id,uid,nick,buyer_credit,seller_credit,created,last_visit,alipay_account,alipay_no')
        data=client.execute(req.getApiParas())
        info['user']=data['user']
        req=ShopGet()
        req.setFields('sid,cid,title,created,modified,shop_score')
        req.setNick(info['user']['nick'])
        data=client.execute(req.getApiParas())
        info['shop']=data['shop']
        req=ShopRemainshowcaseGet()
        data=client.execute(req.getApiParas())
        info['shop'].update(data['shop'])
        memcache.set('info',info,0,0,shop_key['appkey'])

class items():
    item_fields='approve_status,num_iid,title,type,cid,pic_url,num,props,valid_thru,list_time,price,has_discount,has_invoice,has_warranty,has_showcase,modified,delist_time,postage_id,seller_cids,outer_id,volume'

    @classmethod
    def onsale(self,user=''):
        user=user or base.user()
        data=memcache.get('onsale',user)
        if type(data) is types.DictType:
            return data
        else:
            self.refresh_onsale(user)
            return self.onsale(user)

    @classmethod
    def onsale_sort(self,user=''):
        user=user or base.user()
        data=memcache.get('onsale_sort',user)
        if type(data) is types.ListType:
            return data
        else:
            self.refresh_onsale(user)
            return self.onsale_sort(user)

    @classmethod
    def showcase(self,user=''):
        user=user or base.user()
        data=memcache.get('showcase',user)
        if type(data) is types.ListType:
            return data
        else:
            self.refresh_onsale(user)
            return self.showcase(user)

    @classmethod
    def instock_regular(self,user=''):
        user=user or base.user()
        data=memcache.get('instock_regular',user)
        if type(data) is types.ListType:
            return data
        else:
            self.refresh_instock(user)
            return self.instock_regular(user)

    @classmethod
    def instock_violation(self,user=''):
        user=user or base.user()
        data=memcache.get('instock_violation',user)
        if type(data) is types.DictType:
            return data
        else:
            self.refresh_instock(user)
            return self.instock_violation(user)

    @classmethod
    def instock_shelved(self,user=''):
        user=user or base.user()
        data=memcache.get('instock_shelved',user)
        if type(data) is types.DictType:
            return data
        else:
            self.refresh_instock(user)
            return self.instock_shelved(user)

    @classmethod
    def instock_showcase(self,user=''):
        user=user or base.user()
        data=memcache.get('instock_showcase',user)
        if type(data) is types.ListType:
            return data
        else:
            self.refresh_instock(user)
            return self.instock_showcase(user)

    @classmethod
    def showplat(self,user='',cid=0,num=9):
        user=user or base.user()
        shop_key=base.getkey(user)
        data=memcache.get('%s%s'%('hotsale_',cid),user)
        if type(data) is types.ListType:
            return data
        else:
            return self.request_hotsale(shop_key,cid,num)

    @classmethod
    def refresh_onsale(self,user=''):
        if user:
            shop_key=base.getkey(user)
        else:
            shop_key=base.flag()['onsale']
        self.request_onsale(shop_key)

    @classmethod
    def refresh_instock(self,user=''):
        if user:
            shop_key=base.getkey(user)
        else:
            shop_key=base.flag()['instock']
        self.request_instock(shop_key)

    @classmethod
    def request_onsale(self,shop_key):
        client=TopClient()
        client.appkey=shop_key['appkey']
        client.secretKey=shop_key['secretKey']
        onsale={}
        onsale_sort={}
        showcase=[]
        req=ItemsOnsaleGet()
        req.setFields(self.item_fields)
        req.setPageSize(200)
        req.setPageNo(1)
        while True:
            data=client.execute(req.getApiParas())
            if data.has_key('items'):
                for item in data['items']['item']:
                    onsale[item['num_iid']]=item
                    delist_time=long(time.mktime(time.strptime(item['delist_time'],'%Y-%m-%d %H:%M:%S')))
                    if delist_time%86400!=0:
                        onsale_sort[item['num_iid']]=delist_time
                    if item['has_showcase']==True:
                        showcase.append(item['num_iid'])
                if req.getPageNo()>=int(math.ceil(data['total_results']/float(req.getPageSize()))):
                    break
            else:
                break
            req.setPageNo(req.getPageNo()+1)
        memcache.set('onsale',onsale,0,0,shop_key['appkey'])
        memcache.set('onsale_sort',sorted(onsale_sort.iteritems(),key=lambda x:x[1],reverse=False),0,0,shop_key['appkey'])
        memcache.set('showcase',showcase,0,0,shop_key['appkey'])

    @classmethod
    def request_instock(self,shop_key):
        client=TopClient()
        client.appkey=shop_key['appkey']
        client.secretKey=shop_key['secretKey']
        instock_regular={}
        instock_violation={}
        instock_shelved={}
        instock_showcase=[]
        req=ItemsInventoryGet()
        req.setFields(self.item_fields)
        req.setPageSize(200)
        req.setPageNo(1)
        req.setBanner("regular_shelved")
        while True:
            data=client.execute(req.getApiParas())
            if data.has_key('items'):
                for item in data['items']['item']:
                    instock_regular[item['num_iid']]=long(time.mktime(time.strptime(item['delist_time'],'%Y-%m-%d %H:%M:%S')))
                if req.getPageNo()>=int(math.ceil(data['total_results']/float(req.getPageSize()))):
                    break
            else:
                break
            req.setPageNo(req.getPageNo()+1)
        req.setPageNo(1)
        req.setBanner("violation_off_shelf")
        while True:
            data=client.execute(req.getApiParas())
            if data.has_key('items'):
                for item in data['items']['item']:
                    instock_violation[item['num_iid']]=item
                if req.getPageNo()>=int(math.ceil(data['total_results']/float(req.getPageSize()))):
                    break
            else:
                break
            req.setPageNo(req.getPageNo()+1)
        req.setPageNo(1)
        req.setBanner("for_shelved")
        while True:
            data=client.execute(req.getApiParas())
            if data.has_key('items'):
                for item in data['items']['item']:
                    instock_shelved[item['num_iid']]=item
                    if item['has_showcase']==True:
                        instock_showcase.append(item['num_iid'])
                if req.getPageNo()>=int(math.ceil(data['total_results']/float(req.getPageSize()))):
                    break
            else:
                break
            req.setPageNo(req.getPageNo()+1)
        memcache.set('instock_regular',sorted(instock_regular.iteritems(),key=lambda x:x[1],reverse=False),0,0,shop_key['appkey'])
        memcache.set('instock_violation',instock_violation,0,0,shop_key['appkey'])
        memcache.set('instock_shelved',instock_shelved,0,0,shop_key['appkey'])
        memcache.set('instock_showcase',instock_showcase,0,0,shop_key['appkey'])

    @classmethod
    def request_hotsale(self,shop_key,cid,num):
        client=TopClient()
        client.appkey=shop_key['appkey']
        client.secretKey=shop_key['secretKey']
        showplat=[]
        req=ItemsGet()
        req.setFields(self.item_fields)
        req.setNicks(shop.info(shop_key['appkey'])['user']['nick'])
        req.setOrderBy('volume:desc')
        req.setPageSize(num)
        if cid>0: req.setCid(cid)
        data=client.execute(req.getApiParas())
        if data.has_key('items'):
            for item in data['items']['item']:
                showplat.append(item)
        if len(showplat)<num:
            showplat.extend(self.showplat(shop_key['appkey'],0,num)[0:num-len(showplat)])
        memcache.set('%s%s'%('hotsale_',cid),showplat,3600,0,shop_key['appkey'])
        return showplat


if __name__=='__main__':
    pass
else:
    base.user()