class IncrementAuthorizemessagesGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.increment.authorizemessages.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setNicks(self,nicks):
        self.apiParas['nicks']=nicks
    def getNicks(self):
        return self.apiParas['nicks']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
