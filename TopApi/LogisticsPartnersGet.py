class LogisticsPartnersGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.logistics.partners.get'}
    def setGoodsValue(self,goodsValue):
        self.apiParas['goods_value']=goodsValue
    def getGoodsValue(self):
        return self.apiParas['goods_value']
    def setServiceType(self,serviceType):
        self.apiParas['service_type']=serviceType
    def getServiceType(self):
        return self.apiParas['service_type']
    def setSourceId(self,sourceId):
        self.apiParas['source_id']=sourceId
    def getSourceId(self):
        return self.apiParas['source_id']
    def setTargetId(self,targetId):
        self.apiParas['target_id']=targetId
    def getTargetId(self):
        return self.apiParas['target_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
