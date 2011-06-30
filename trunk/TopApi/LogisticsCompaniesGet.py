class LogisticsCompaniesGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.logistics.companies.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setIsRecommended(self,isRecommended):
        self.apiParas['is_recommended']=isRecommended
    def getIsRecommended(self):
        return self.apiParas['is_recommended']
    def setOrderMode(self,orderMode):
        self.apiParas['order_mode']=orderMode
    def getOrderMode(self):
        return self.apiParas['order_mode']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
