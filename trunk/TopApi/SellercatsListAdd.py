class SellercatsListAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.sellercats.list.add'}
    def setName(self,name):
        self.apiParas['name']=name
    def getName(self):
        return self.apiParas['name']
    def setParentCid(self,parentCid):
        self.apiParas['parent_cid']=parentCid
    def getParentCid(self):
        return self.apiParas['parent_cid']
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
