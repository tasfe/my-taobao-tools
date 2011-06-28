class WlbOrderstatusGet(object):
    apiParas={'method':'taobao.wlb.orderstatus.get'}
    def setOrderCode(self,orderCode):
        self.apiParas['order_code']=orderCode
    def getOrderCode(self):
        return self.apiParas['order_code']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
