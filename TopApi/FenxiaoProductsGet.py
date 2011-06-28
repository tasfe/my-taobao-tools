class FenxiaoProductsGet(object):
    apiParas={'method':'taobao.fenxiao.products.get'}
    def setEndModified(self,endModified):
        self.apiParas['end_modified']=endModified
    def getEndModified(self):
        return self.apiParas['end_modified']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setOuterId(self,outerId):
        self.apiParas['outer_id']=outerId
    def getOuterId(self):
        return self.apiParas['outer_id']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setPids(self,pids):
        self.apiParas['pids']=pids
    def getPids(self):
        return self.apiParas['pids']
    def setProductcatId(self,productcatId):
        self.apiParas['productcat_id']=productcatId
    def getProductcatId(self):
        return self.apiParas['productcat_id']
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
