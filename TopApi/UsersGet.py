class UsersGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.users.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setNicks(self,nicks):
        self.apiParas['nicks']=nicks
    def getNicks(self):
        return self.apiParas['nicks']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
