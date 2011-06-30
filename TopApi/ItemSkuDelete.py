class ItemSkuDelete(object):
    def __init__(self):
        self.apiParas={'method':'taobao.item.sku.delete'}
    def setItemNum(self,itemNum):
        self.apiParas['item_num']=itemNum
    def getItemNum(self):
        return self.apiParas['item_num']
    def setItemPrice(self,itemPrice):
        self.apiParas['item_price']=itemPrice
    def getItemPrice(self):
        return self.apiParas['item_price']
    def setLang(self,lang):
        self.apiParas['lang']=lang
    def getLang(self):
        return self.apiParas['lang']
    def setNumIid(self,numIid):
        self.apiParas['num_iid']=numIid
    def getNumIid(self):
        return self.apiParas['num_iid']
    def setProperties(self,properties):
        self.apiParas['properties']=properties
    def getProperties(self):
        return self.apiParas['properties']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
