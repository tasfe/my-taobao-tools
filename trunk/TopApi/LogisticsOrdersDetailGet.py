class LogisticsOrdersDetailGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.logistics.orders.detail.get'}
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
    def setFreightPayer(self,freightPayer):
        self.apiParas['freight_payer']=freightPayer
    def getFreightPayer(self):
        return self.apiParas['freight_payer']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setReceiverName(self,receiverName):
        self.apiParas['receiver_name']=receiverName
    def getReceiverName(self):
        return self.apiParas['receiver_name']
    def setSellerConfirm(self,sellerConfirm):
        self.apiParas['seller_confirm']=sellerConfirm
    def getSellerConfirm(self):
        return self.apiParas['seller_confirm']
    def setStartCreated(self,startCreated):
        self.apiParas['start_created']=startCreated
    def getStartCreated(self):
        return self.apiParas['start_created']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def setType(self,type):
        self.apiParas['type']=type
    def getType(self):
        return self.apiParas['type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
