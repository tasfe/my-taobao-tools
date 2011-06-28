class WlbItemConsignmentPageGet(object):
    apiParas={'method':'taobao.wlb.item.consignment.page.get'}
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setTgtItemId(self,tgtItemId):
        self.apiParas['tgt_item_id']=tgtItemId
    def getTgtItemId(self):
        return self.apiParas['tgt_item_id']
    def setTgtUserId(self,tgtUserId):
        self.apiParas['tgt_user_id']=tgtUserId
    def getTgtUserId(self):
        return self.apiParas['tgt_user_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
