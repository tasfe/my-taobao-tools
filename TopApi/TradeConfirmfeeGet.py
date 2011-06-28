class TradeConfirmfeeGet(object):
    apiParas={'method':'taobao.trade.confirmfee.get'}
    def setIsDetail(self,isDetail):
        self.apiParas['is_detail']=isDetail
    def getIsDetail(self):
        return self.apiParas['is_detail']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
