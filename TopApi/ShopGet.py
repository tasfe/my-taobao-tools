class ShopGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.shop.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
