class AppstoreSubscribeGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.appstore.subscribe.get'}
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
