class TaohuaStaffrecitemsGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.taohua.staffrecitems.get'}
    def setItemType(self,itemType):
        self.apiParas['item_type']=itemType
    def getItemType(self):
        return self.apiParas['item_type']
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
