class TimeGet(object):
    apiParas={'method':'taobao.time.get'}
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
