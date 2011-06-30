class LogisticsDummySend(object):
    def __init__(self):
        self.apiParas={'method':'taobao.logistics.dummy.send'}
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
