class SellercatsListUpdate(object):
    def __init__(self):
        self.apiParas={'method':'taobao.sellercats.list.update'}
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
    def setName(self,name):
        self.apiParas['name']=name
    def getName(self):
        return self.apiParas['name']
    def setPictUrl(self,pictUrl):
        self.apiParas['pict_url']=pictUrl
    def getPictUrl(self):
        return self.apiParas['pict_url']
    def setSortOrder(self,sortOrder):
        self.apiParas['sort_order']=sortOrder
    def getSortOrder(self):
        return self.apiParas['sort_order']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
