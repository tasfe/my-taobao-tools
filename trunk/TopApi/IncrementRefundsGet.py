class IncrementRefundsGet(object):
    apiParas={'method':'taobao.increment.refunds.get'}
    def setEndModified(self,endModified):
        self.apiParas['end_modified']=endModified
    def getEndModified(self):
        return self.apiParas['end_modified']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setStartModified(self,startModified):
        self.apiParas['start_modified']=startModified
    def getStartModified(self):
        return self.apiParas['start_modified']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
