class RefundGet(object):
    apiParas={'method':'taobao.refund.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setRefundId(self,refundId):
        self.apiParas['refund_id']=refundId
    def getRefundId(self):
        return self.apiParas['refund_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
