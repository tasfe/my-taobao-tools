class LogisticsAddressRemove(object):
    apiParas={'method':'taobao.logistics.address.remove'}
    def setContactId(self,contactId):
        self.apiParas['contact_id']=contactId
    def getContactId(self):
        return self.apiParas['contact_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
