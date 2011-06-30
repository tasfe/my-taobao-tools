class TopatsTradeAccountreportGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.topats.trade.accountreport.get'}
    def setEndCreated(self,endCreated):
        self.apiParas['end_created']=endCreated
    def getEndCreated(self):
        return self.apiParas['end_created']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setStartCreated(self,startCreated):
        self.apiParas['start_created']=startCreated
    def getStartCreated(self):
        return self.apiParas['start_created']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
