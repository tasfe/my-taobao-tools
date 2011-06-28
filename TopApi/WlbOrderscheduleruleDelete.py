class WlbOrderscheduleruleDelete(object):
    apiParas={'method':'taobao.wlb.orderschedulerule.delete'}
    def setId(self,id):
        self.apiParas['id']=id
    def getId(self):
        return self.apiParas['id']
    def setUserNick(self,userNick):
        self.apiParas['user_nick']=userNick
    def getUserNick(self):
        return self.apiParas['user_nick']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
