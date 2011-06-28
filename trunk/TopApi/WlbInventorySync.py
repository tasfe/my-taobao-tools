class WlbInventorySync(object):
    apiParas={'method':'taobao.wlb.inventory.sync'}
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setItemType(self,itemType):
        self.apiParas['item_type']=itemType
    def getItemType(self):
        return self.apiParas['item_type']
    def setQuantity(self,quantity):
        self.apiParas['quantity']=quantity
    def getQuantity(self):
        return self.apiParas['quantity']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
