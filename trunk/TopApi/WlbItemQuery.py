class WlbItemQuery(object):
    apiParas={'method':'taobao.wlb.item.query'}
    def setIsSku(self,isSku):
        self.apiParas['is_sku']=isSku
    def getIsSku(self):
        return self.apiParas['is_sku']
    def setItemCode(self,itemCode):
        self.apiParas['item_code']=itemCode
    def getItemCode(self):
        return self.apiParas['item_code']
    def setItemType(self,itemType):
        self.apiParas['item_type']=itemType
    def getItemType(self):
        return self.apiParas['item_type']
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
    def setParentId(self,parentId):
        self.apiParas['parent_id']=parentId
    def getParentId(self):
        return self.apiParas['parent_id']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def setTitle(self,title):
        self.apiParas['title']=title
    def getTitle(self):
        return self.apiParas['title']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
