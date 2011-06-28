class LogisticsOnlineConfirm(object):
    apiParas={'method':'taobao.logistics.online.confirm'}
    def setOutSid(self,outSid):
        self.apiParas['out_sid']=outSid
    def getOutSid(self):
        return self.apiParas['out_sid']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
