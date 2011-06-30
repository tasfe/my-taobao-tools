class WangwangEserviceChatlogGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wangwang.eservice.chatlog.get'}
    def setEndDate(self,endDate):
        self.apiParas['end_date']=endDate
    def getEndDate(self):
        return self.apiParas['end_date']
    def setFromId(self,fromId):
        self.apiParas['from_id']=fromId
    def getFromId(self):
        return self.apiParas['from_id']
    def setStartDate(self,startDate):
        self.apiParas['start_date']=startDate
    def getStartDate(self):
        return self.apiParas['start_date']
    def setToId(self,toId):
        self.apiParas['to_id']=toId
    def getToId(self):
        return self.apiParas['to_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
