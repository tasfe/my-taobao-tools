class FenxiaoDistributorsGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.fenxiao.distributors.get'}
    def setNicks(self,nicks):
        self.apiParas['nicks']=nicks
    def getNicks(self):
        return self.apiParas['nicks']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
