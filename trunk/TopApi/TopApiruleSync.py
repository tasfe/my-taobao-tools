class TopApiruleSync(object):
    def __init__(self):
        self.apiParas={'method':'taobao.top.apirule.sync'}
    def setApiName(self,apiName):
        self.apiParas['api_name']=apiName
    def getApiName(self):
        return self.apiParas['api_name']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
