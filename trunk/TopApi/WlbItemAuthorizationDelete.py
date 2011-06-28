class WlbItemAuthorizationDelete(object):
    apiParas={'method':'taobao.wlb.item.authorization.delete'}
    def setAuthorizeId(self,authorizeId):
        self.apiParas['authorize_id']=authorizeId
    def getAuthorizeId(self):
        return self.apiParas['authorize_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
