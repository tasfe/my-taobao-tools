class ItemSkuGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.item.sku.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def setNumIid(self,numIid):
        self.apiParas['num_iid']=numIid
    def getNumIid(self):
        return self.apiParas['num_iid']
    def setSkuId(self,skuId):
        self.apiParas['sku_id']=skuId
    def getSkuId(self):
        return self.apiParas['sku_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
