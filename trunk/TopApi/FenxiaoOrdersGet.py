class FenxiaoOrdersGet(object):
    apiParas={'method':'taobao.fenxiao.orders.get'}
    def setEndCreated(self,endCreated):
        self.apiParas['end_created']=endCreated
    def getEndCreated(self):
        return self.apiParas['end_created']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setPurchaseOrderId(self,purchaseOrderId):
        self.apiParas['purchase_order_id']=purchaseOrderId
    def getPurchaseOrderId(self):
        return self.apiParas['purchase_order_id']
    def setStartCreated(self,startCreated):
        self.apiParas['start_created']=startCreated
    def getStartCreated(self):
        return self.apiParas['start_created']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def setTimeType(self,timeType):
        self.apiParas['time_type']=timeType
    def getTimeType(self):
        return self.apiParas['time_type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
