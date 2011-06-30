class ItemQuantityUpdate(object):
    def __init__(self):
        self.apiParas={'method':'taobao.item.quantity.update'}
    def setNumIid(self,numIid):
        self.apiParas['num_iid']=numIid
    def getNumIid(self):
        return self.apiParas['num_iid']
    def setOuterId(self,outerId):
        self.apiParas['outer_id']=outerId
    def getOuterId(self):
        return self.apiParas['outer_id']
    def setQuantity(self,quantity):
        self.apiParas['quantity']=quantity
    def getQuantity(self):
        return self.apiParas['quantity']
    def setSkuId(self,skuId):
        self.apiParas['sku_id']=skuId
    def getSkuId(self):
        return self.apiParas['sku_id']
    def setType(self,type):
        self.apiParas['type']=type
    def getType(self):
        return self.apiParas['type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
