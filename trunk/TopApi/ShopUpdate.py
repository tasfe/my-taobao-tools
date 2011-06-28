class ShopUpdate(object):
    apiParas={'method':'taobao.shop.update'}
    def setBulletin(self,bulletin):
        self.apiParas['bulletin']=bulletin
    def getBulletin(self):
        return self.apiParas['bulletin']
    def setDesc(self,desc):
        self.apiParas['desc']=desc
    def getDesc(self):
        return self.apiParas['desc']
    def setTitle(self,title):
        self.apiParas['title']=title
    def getTitle(self):
        return self.apiParas['title']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
