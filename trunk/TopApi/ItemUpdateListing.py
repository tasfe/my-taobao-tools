class ItemUpdateListing(object):
    def __init__(self):
        self.apiParas={'method':'taobao.item.update.listing'}
    def setNum(self,num):
        self.apiParas['num']=num
    def getNum(self):
        return self.apiParas['num']
    def setNumIid(self,numIid):
        self.apiParas['num_iid']=numIid
    def getNumIid(self):
        return self.apiParas['num_iid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
