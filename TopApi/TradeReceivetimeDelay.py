class TradeReceivetimeDelay(object):
    apiParas={'method':'taobao.trade.receivetime.delay'}
    def setDays(self,days):
        self.apiParas['days']=days
    def getDays(self):
        return self.apiParas['days']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
