class LogisticsAddressSearch(object):
    apiParas={'method':'taobao.logistics.address.search'}
    def setRdef(self,rdef):
        self.apiParas['rdef']=rdef
    def getRdef(self):
        return self.apiParas['rdef']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
