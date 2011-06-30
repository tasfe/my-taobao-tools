class FavoriteSearch(object):
    def __init__(self):
        self.apiParas={'method':'taobao.favorite.search'}
    def setCollectType(self,collectType):
        self.apiParas['collect_type']=collectType
    def getCollectType(self):
        return self.apiParas['collect_type']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setUserNick(self,userNick):
        self.apiParas['user_nick']=userNick
    def getUserNick(self):
        return self.apiParas['user_nick']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
