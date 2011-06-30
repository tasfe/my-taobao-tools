class RefundRefuse(object):
    def __init__(self):
        self.apiParas={'method':'taobao.refund.refuse'}
    def setOid(self,oid):
        self.apiParas['oid']=oid
    def getOid(self):
        return self.apiParas['oid']
    def setRefundId(self,refundId):
        self.apiParas['refund_id']=refundId
    def getRefundId(self):
        return self.apiParas['refund_id']
    def setRefuseMessage(self,refuseMessage):
        self.apiParas['refuse_message']=refuseMessage
    def getRefuseMessage(self):
        return self.apiParas['refuse_message']
    def setRefuseProof(self,refuseProof):
        self.apiParas['refuse_proof']=refuseProof
    def getRefuseProof(self):
        return self.apiParas['refuse_proof']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
