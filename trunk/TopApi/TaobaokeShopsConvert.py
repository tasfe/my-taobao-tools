class TaobaokeShopsConvert(object):
    def __init__(self):
        self.apiParas={'method':'taobao.taobaoke.shops.convert'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def setOuterCode(self,outerCode):
        self.apiParas['outer_code']=outerCode
    def getOuterCode(self):
        return self.apiParas['outer_code']
    def setPid(self,pid):
        self.apiParas['pid']=pid
    def getPid(self):
        return self.apiParas['pid']
    def setSids(self,sids):
        self.apiParas['sids']=sids
    def getSids(self):
        return self.apiParas['sids']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
