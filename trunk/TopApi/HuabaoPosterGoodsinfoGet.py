class HuabaoPosterGoodsinfoGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.huabao.poster.goodsinfo.get'}
    def setPosterId(self,posterId):
        self.apiParas['poster_id']=posterId
    def getPosterId(self):
        return self.apiParas['poster_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
