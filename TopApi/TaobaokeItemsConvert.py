class TaobaokeItemsConvert(object):
    def __init__(self):
        self.apiParas={'method':'taobao.taobaoke.items.convert'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setIsMobile(self,isMobile):
        self.apiParas['is_mobile']=isMobile
    def getIsMobile(self):
        return self.apiParas['is_mobile']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def setNumIids(self,numIids):
        self.apiParas['num_iids']=numIids
    def getNumIids(self):
        return self.apiParas['num_iids']
    def setOuterCode(self,outerCode):
        self.apiParas['outer_code']=outerCode
    def getOuterCode(self):
        return self.apiParas['outer_code']
    def setPid(self,pid):
        self.apiParas['pid']=pid
    def getPid(self):
        return self.apiParas['pid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
