class AftersaleGet(object):
    apiParas={'method':'taobao.aftersale.get'}
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
