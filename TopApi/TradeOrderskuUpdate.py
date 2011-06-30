class TradeOrderskuUpdate(object):
    def __init__(self):
        self.apiParas={'method':'taobao.trade.ordersku.update'}
    def setOid(self,oid):
        self.apiParas['oid']=oid
    def getOid(self):
        return self.apiParas['oid']
    def setSkuId(self,skuId):
        self.apiParas['sku_id']=skuId
    def getSkuId(self):
        return self.apiParas['sku_id']
    def setSkuProps(self,skuProps):
        self.apiParas['sku_props']=skuProps
    def getSkuProps(self):
        return self.apiParas['sku_props']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
