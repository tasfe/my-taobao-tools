class TimeGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.time.get'}
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
