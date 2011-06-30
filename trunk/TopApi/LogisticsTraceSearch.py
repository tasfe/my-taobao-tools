class LogisticsTraceSearch(object):
    def __init__(self):
        self.apiParas={'method':'taobao.logistics.trace.search'}
    def setSellerNick(self,sellerNick):
        self.apiParas['seller_nick']=sellerNick
    def getSellerNick(self):
        return self.apiParas['seller_nick']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
