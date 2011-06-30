class TraderatesGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.traderates.get'}
    def setEndDate(self,endDate):
        self.apiParas['end_date']=endDate
    def getEndDate(self):
        return self.apiParas['end_date']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setPeerNick(self,peerNick):
        self.apiParas['peer_nick']=peerNick
    def getPeerNick(self):
        return self.apiParas['peer_nick']
    def setRateType(self,rateType):
        self.apiParas['rate_type']=rateType
    def getRateType(self):
        return self.apiParas['rate_type']
    def setResult(self,result):
        self.apiParas['result']=result
    def getResult(self):
        return self.apiParas['result']
    def setRole(self,role):
        self.apiParas['role']=role
    def getRole(self):
        return self.apiParas['role']
    def setStartDate(self,startDate):
        self.apiParas['start_date']=startDate
    def getStartDate(self):
        return self.apiParas['start_date']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
