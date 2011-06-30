class LogisticsOnlineSend(object):
    def __init__(self):
        self.apiParas={'method':'taobao.logistics.online.send'}
    def setCancelId(self,cancelId):
        self.apiParas['cancel_id']=cancelId
    def getCancelId(self):
        return self.apiParas['cancel_id']
    def setCompanyCode(self,companyCode):
        self.apiParas['company_code']=companyCode
    def getCompanyCode(self):
        return self.apiParas['company_code']
    def setOutSid(self,outSid):
        self.apiParas['out_sid']=outSid
    def getOutSid(self):
        return self.apiParas['out_sid']
    def setSenderId(self,senderId):
        self.apiParas['sender_id']=senderId
    def getSenderId(self):
        return self.apiParas['sender_id']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
