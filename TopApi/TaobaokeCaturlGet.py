class TaobaokeCaturlGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.taobaoke.caturl.get'}
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
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
    def setQ(self,q):
        self.apiParas['q']=q
    def getQ(self):
        return self.apiParas['q']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
