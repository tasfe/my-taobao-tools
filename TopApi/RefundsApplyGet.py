class RefundsApplyGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.refunds.apply.get'}
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
    def setSellerNick(self,sellerNick):
        self.apiParas['seller_nick']=sellerNick
    def getSellerNick(self):
        return self.apiParas['seller_nick']
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
