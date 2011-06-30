class TradesSoldGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.trades.sold.get'}
    def setBuyerNick(self,buyerNick):
        self.apiParas['buyer_nick']=buyerNick
    def getBuyerNick(self):
        return self.apiParas['buyer_nick']
    def setEndCreated(self,endCreated):
        self.apiParas['end_created']=endCreated
    def getEndCreated(self):
        return self.apiParas['end_created']
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
    def setRateStatus(self,rateStatus):
        self.apiParas['rate_status']=rateStatus
    def getRateStatus(self):
        return self.apiParas['rate_status']
    def setStartCreated(self,startCreated):
        self.apiParas['start_created']=startCreated
    def getStartCreated(self):
        return self.apiParas['start_created']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def setTag(self,tag):
        self.apiParas['tag']=tag
    def getTag(self):
        return self.apiParas['tag']
    def setType(self,type):
        self.apiParas['type']=type
    def getType(self):
        return self.apiParas['type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
