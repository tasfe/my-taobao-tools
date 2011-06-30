class AftersaleGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.aftersale.get'}
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
