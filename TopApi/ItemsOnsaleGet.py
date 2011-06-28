class ItemsOnsaleGet(object):
    apiParas={'method':'taobao.items.onsale.get'}
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
    def setEndModified(self,endModified):
        self.apiParas['end_modified']=endModified
    def getEndModified(self):
        return self.apiParas['end_modified']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setHasDiscount(self,hasDiscount):
        self.apiParas['has_discount']=hasDiscount
    def getHasDiscount(self):
        return self.apiParas['has_discount']
    def setHasShowcase(self,hasShowcase):
        self.apiParas['has_showcase']=hasShowcase
    def getHasShowcase(self):
        return self.apiParas['has_showcase']
    def setIsEx(self,isEx):
        self.apiParas['is_ex']=isEx
    def getIsEx(self):
        return self.apiParas['is_ex']
    def setIsTaobao(self,isTaobao):
        self.apiParas['is_taobao']=isTaobao
    def getIsTaobao(self):
        return self.apiParas['is_taobao']
    def setOrderBy(self,orderBy):
        self.apiParas['order_by']=orderBy
    def getOrderBy(self):
        return self.apiParas['order_by']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setQ(self,q):
        self.apiParas['q']=q
    def getQ(self):
        return self.apiParas['q']
    def setSellerCids(self,sellerCids):
        self.apiParas['seller_cids']=sellerCids
    def getSellerCids(self):
        return self.apiParas['seller_cids']
    def setStartModified(self,startModified):
        self.apiParas['start_modified']=startModified
    def getStartModified(self):
        return self.apiParas['start_modified']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
