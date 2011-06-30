class RefundsReceiveGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.refunds.receive.get'}
    def setBuyerNick(self,buyerNick):
        self.apiParas['buyer_nick']=buyerNick
    def getBuyerNick(self):
        return self.apiParas['buyer_nick']
    def setEndModified(self,endModified):
        self.apiParas['end_modified']=endModified
    def getEndModified(self):
        return self.apiParas['end_modified']
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
    def setStartModified(self,startModified):
        self.apiParas['start_modified']=startModified
    def getStartModified(self):
        return self.apiParas['start_modified']
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
