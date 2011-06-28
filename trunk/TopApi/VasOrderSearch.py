class VasOrderSearch(object):
    apiParas={'method':'taobao.vas.order.search'}
    def setArticleCode(self,articleCode):
        self.apiParas['article_code']=articleCode
    def getArticleCode(self):
        return self.apiParas['article_code']
    def setBizOrderId(self,bizOrderId):
        self.apiParas['biz_order_id']=bizOrderId
    def getBizOrderId(self):
        return self.apiParas['biz_order_id']
    def setBizType(self,bizType):
        self.apiParas['biz_type']=bizType
    def getBizType(self):
        return self.apiParas['biz_type']
    def setEndCreated(self,endCreated):
        self.apiParas['end_created']=endCreated
    def getEndCreated(self):
        return self.apiParas['end_created']
    def setItemCode(self,itemCode):
        self.apiParas['item_code']=itemCode
    def getItemCode(self):
        return self.apiParas['item_code']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def setOrderId(self,orderId):
        self.apiParas['order_id']=orderId
    def getOrderId(self):
        return self.apiParas['order_id']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setStartCreated(self,startCreated):
        self.apiParas['start_created']=startCreated
    def getStartCreated(self):
        return self.apiParas['start_created']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
