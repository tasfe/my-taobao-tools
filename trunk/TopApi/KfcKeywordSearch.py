class KfcKeywordSearch(object):
    def __init__(self):
        self.apiParas={'method':'taobao.kfc.keyword.search'}
    def setApply(self,apply):
        self.apiParas['apply']=apply
    def getApply(self):
        return self.apiParas['apply']
    def setContent(self,content):
        self.apiParas['content']=content
    def getContent(self):
        return self.apiParas['content']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
