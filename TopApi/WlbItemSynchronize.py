class WlbItemSynchronize(object):
    apiParas={'method':'taobao.wlb.item.synchronize'}
    def setExtEntityId(self,extEntityId):
        self.apiParas['ext_entity_id']=extEntityId
    def getExtEntityId(self):
        return self.apiParas['ext_entity_id']
    def setExtEntityType(self,extEntityType):
        self.apiParas['ext_entity_type']=extEntityType
    def getExtEntityType(self):
        return self.apiParas['ext_entity_type']
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
