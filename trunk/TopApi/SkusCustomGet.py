class SkusCustomGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.skus.custom.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setOuterId(self,outerId):
        self.apiParas['outer_id']=outerId
    def getOuterId(self):
        return self.apiParas['outer_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
