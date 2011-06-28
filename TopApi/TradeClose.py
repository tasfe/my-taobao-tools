class TradeClose(object):
    apiParas={'method':'taobao.trade.close'}
    def setCloseReason(self,closeReason):
        self.apiParas['close_reason']=closeReason
    def getCloseReason(self):
        return self.apiParas['close_reason']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
