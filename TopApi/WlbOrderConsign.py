class WlbOrderConsign(object):
    apiParas={'method':'taobao.wlb.order.consign'}
    def setWlbOrderCode(self,wlbOrderCode):
        self.apiParas['wlb_order_code']=wlbOrderCode
    def getWlbOrderCode(self):
        return self.apiParas['wlb_order_code']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
