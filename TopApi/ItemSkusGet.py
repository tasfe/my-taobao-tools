class ItemSkusGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.item.skus.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setNumIids(self,numIids):
        self.apiParas['num_iids']=numIids
    def getNumIids(self):
        return self.apiParas['num_iids']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
