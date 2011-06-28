class WlbTradeorderGet(object):
    apiParas={'method':'taobao.wlb.tradeorder.get'}
    def setTradeId(self,tradeId):
        self.apiParas['trade_id']=tradeId
    def getTradeId(self):
        return self.apiParas['trade_id']
    def setTradeType(self,tradeType):
        self.apiParas['trade_type']=tradeType
    def getTradeType(self):
        return self.apiParas['trade_type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
