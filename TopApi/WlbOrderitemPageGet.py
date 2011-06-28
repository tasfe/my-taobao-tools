class WlbOrderitemPageGet(object):
    apiParas={'method':'taobao.wlb.orderitem.page.get'}
    def setOrderCode(self,orderCode):
        self.apiParas['order_code']=orderCode
    def getOrderCode(self):
        return self.apiParas['order_code']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
