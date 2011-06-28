class PostageDelete(object):
    apiParas={'method':'taobao.postage.delete'}
    def setPostageId(self,postageId):
        self.apiParas['postage_id']=postageId
    def getPostageId(self):
        return self.apiParas['postage_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
