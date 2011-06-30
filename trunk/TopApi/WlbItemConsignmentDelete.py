class WlbItemConsignmentDelete(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.item.consignment.delete'}
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setOwnerItemList(self,ownerItemList):
        self.apiParas['owner_item_list']=ownerItemList
    def getOwnerItemList(self):
        return self.apiParas['owner_item_list']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
