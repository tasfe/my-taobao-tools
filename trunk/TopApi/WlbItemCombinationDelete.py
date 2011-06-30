class WlbItemCombinationDelete(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.item.combination.delete'}
    def setDestItemList(self,destItemList):
        self.apiParas['dest_item_list']=destItemList
    def getDestItemList(self):
        return self.apiParas['dest_item_list']
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
