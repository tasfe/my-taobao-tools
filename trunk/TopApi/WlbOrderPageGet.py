class WlbOrderPageGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.order.page.get'}
    def setEndTime(self,endTime):
        self.apiParas['end_time']=endTime
    def getEndTime(self):
        return self.apiParas['end_time']
    def setOrderCode(self,orderCode):
        self.apiParas['order_code']=orderCode
    def getOrderCode(self):
        return self.apiParas['order_code']
    def setOrderStatus(self,orderStatus):
        self.apiParas['order_status']=orderStatus
    def getOrderStatus(self):
        return self.apiParas['order_status']
    def setOrderSubType(self,orderSubType):
        self.apiParas['order_sub_type']=orderSubType
    def getOrderSubType(self):
        return self.apiParas['order_sub_type']
    def setOrderType(self,orderType):
        self.apiParas['order_type']=orderType
    def getOrderType(self):
        return self.apiParas['order_type']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setStartTime(self,startTime):
        self.apiParas['start_time']=startTime
    def getStartTime(self):
        return self.apiParas['start_time']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
