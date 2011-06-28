class WlbNotifyMessageConfirm(object):
    apiParas={'method':'taobao.wlb.notify.message.confirm'}
    def setMessageId(self,messageId):
        self.apiParas['message_id']=messageId
    def getMessageId(self):
        return self.apiParas['message_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
