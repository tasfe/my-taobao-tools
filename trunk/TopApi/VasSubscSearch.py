class VasSubscSearch(object):
    apiParas={'method':'taobao.vas.subsc.search'}
    def setArticleCode(self,articleCode):
        self.apiParas['article_code']=articleCode
    def getArticleCode(self):
        return self.apiParas['article_code']
    def setAutosub(self,autosub):
        self.apiParas['autosub']=autosub
    def getAutosub(self):
        return self.apiParas['autosub']
    def setEndDeadline(self,endDeadline):
        self.apiParas['end_deadline']=endDeadline
    def getEndDeadline(self):
        return self.apiParas['end_deadline']
    def setExpireNotice(self,expireNotice):
        self.apiParas['expire_notice']=expireNotice
    def getExpireNotice(self):
        return self.apiParas['expire_notice']
    def setItemCode(self,itemCode):
        self.apiParas['item_code']=itemCode
    def getItemCode(self):
        return self.apiParas['item_code']
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
    def setStartDeadline(self,startDeadline):
        self.apiParas['start_deadline']=startDeadline
    def getStartDeadline(self):
        return self.apiParas['start_deadline']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
