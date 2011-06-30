class FavoriteAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.favorite.add'}
    def setCollectType(self,collectType):
        self.apiParas['collect_type']=collectType
    def getCollectType(self):
        return self.apiParas['collect_type']
    def setItemNumid(self,itemNumid):
        self.apiParas['item_numid']=itemNumid
    def getItemNumid(self):
        return self.apiParas['item_numid']
    def setShared(self,shared):
        self.apiParas['shared']=shared
    def getShared(self):
        return self.apiParas['shared']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
