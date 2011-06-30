class TradeMemoUpdate(object):
    def __init__(self):
        self.apiParas={'method':'taobao.trade.memo.update'}
    def setFlag(self,flag):
        self.apiParas['flag']=flag
    def getFlag(self):
        return self.apiParas['flag']
    def setMemo(self,memo):
        self.apiParas['memo']=memo
    def getMemo(self):
        return self.apiParas['memo']
    def setReset(self,reset):
        self.apiParas['reset']=reset
    def getReset(self):
        return self.apiParas['reset']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
