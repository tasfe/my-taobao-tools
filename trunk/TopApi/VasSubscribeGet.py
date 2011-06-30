class VasSubscribeGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.vas.subscribe.get'}
    def setArticleCode(self,articleCode):
        self.apiParas['article_code']=articleCode
    def getArticleCode(self):
        return self.apiParas['article_code']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
