class FenxiaoProductcatsGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.fenxiao.productcats.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
