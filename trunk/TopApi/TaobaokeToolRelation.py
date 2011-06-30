class TaobaokeToolRelation(object):
    def __init__(self):
        self.apiParas={'method':'taobao.taobaoke.tool.relation'}
    def setPubid(self,pubid):
        self.apiParas['pubid']=pubid
    def getPubid(self):
        return self.apiParas['pubid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
