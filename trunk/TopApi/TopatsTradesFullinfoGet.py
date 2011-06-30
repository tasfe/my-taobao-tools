class TopatsTradesFullinfoGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.topats.trades.fullinfo.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setTids(self,tids):
        self.apiParas['tids']=tids
    def getTids(self):
        return self.apiParas['tids']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
