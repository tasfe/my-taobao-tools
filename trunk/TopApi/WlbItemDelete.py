class WlbItemDelete(object):
    apiParas={'method':'taobao.wlb.item.delete'}
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setUserNick(self,userNick):
        self.apiParas['user_nick']=userNick
    def getUserNick(self):
        return self.apiParas['user_nick']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
