class ItemSkuUpdate(object):
    def __init__(self):
        self.apiParas={'method':'taobao.item.sku.update'}
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
    def setOuterId(self,outerId):
        self.apiParas['outer_id']=outerId
    def getOuterId(self):
        return self.apiParas['outer_id']
    def setPrice(self,price):
        self.apiParas['price']=price
    def getPrice(self):
        return self.apiParas['price']
    def setProperties(self,properties):
        self.apiParas['properties']=properties
    def getProperties(self):
        return self.apiParas['properties']
    def setQuantity(self,quantity):
        self.apiParas['quantity']=quantity
    def getQuantity(self):
        return self.apiParas['quantity']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
