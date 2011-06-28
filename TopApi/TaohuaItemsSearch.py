class TaohuaItemsSearch(object):
    apiParas={'method':'taobao.taohua.items.search'}
    def setBeginSize(self,beginSize):
        self.apiParas['begin_size']=beginSize
    def getBeginSize(self):
        return self.apiParas['begin_size']
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
    def setEndSize(self,endSize):
        self.apiParas['end_size']=endSize
    def getEndSize(self):
        return self.apiParas['end_size']
    def setFileType(self,fileType):
        self.apiParas['file_type']=fileType
    def getFileType(self):
        return self.apiParas['file_type']
    def setFree(self,free):
        self.apiParas['free']=free
    def getFree(self):
        return self.apiParas['free']
    def setKeywords(self,keywords):
        self.apiParas['keywords']=keywords
    def getKeywords(self):
        return self.apiParas['keywords']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setSort(self,sort):
        self.apiParas['sort']=sort
    def getSort(self):
        return self.apiParas['sort']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
