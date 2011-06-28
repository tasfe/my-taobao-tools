class TradesBoughtGet(object):
    apiParas={'method':'taobao.trades.bought.get'}
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
    def setSellerNick(self,sellerNick):
        self.apiParas['seller_nick']=sellerNick
    def getSellerNick(self):
        return self.apiParas['seller_nick']
    def setStartCreated(self,startCreated):
        self.apiParas['start_created']=startCreated
    def getStartCreated(self):
        return self.apiParas['start_created']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def setType(self,type):
        self.apiParas['type']=type
    def getType(self):
        return self.apiParas['type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
