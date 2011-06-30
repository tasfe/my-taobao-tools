class WlbInventorylogQuery(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.inventorylog.query'}
    def setGmtEnd(self,gmtEnd):
        self.apiParas['gmt_end']=gmtEnd
    def getGmtEnd(self):
        return self.apiParas['gmt_end']
    def setGmtStart(self,gmtStart):
        self.apiParas['gmt_start']=gmtStart
    def getGmtStart(self):
        return self.apiParas['gmt_start']
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setOpType(self,opType):
        self.apiParas['op_type']=opType
    def getOpType(self):
        return self.apiParas['op_type']
    def setOpUserId(self,opUserId):
        self.apiParas['op_user_id']=opUserId
    def getOpUserId(self):
        return self.apiParas['op_user_id']
    def setOrderCode(self,orderCode):
        self.apiParas['order_code']=orderCode
    def getOrderCode(self):
        return self.apiParas['order_code']
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
