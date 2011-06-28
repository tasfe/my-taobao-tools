class WlbReplenishStatistics(object):
    apiParas={'method':'taobao.wlb.replenish.statistics'}
    def setItemCode(self,itemCode):
        self.apiParas['item_code']=itemCode
    def getItemCode(self):
        return self.apiParas['item_code']
    def setName(self,name):
        self.apiParas['name']=name
    def getName(self):
        return self.apiParas['name']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setStoreCode(self,storeCode):
        self.apiParas['store_code']=storeCode
    def getStoreCode(self):
        return self.apiParas['store_code']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
