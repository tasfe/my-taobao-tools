class WlbItemCombinationCreate(object):
    apiParas={'method':'taobao.wlb.item.combination.create'}
    def setDestItemList(self,destItemList):
        self.apiParas['dest_item_list']=destItemList
    def getDestItemList(self):
        return self.apiParas['dest_item_list']
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setProportionList(self,proportionList):
        self.apiParas['proportion_list']=proportionList
    def getProportionList(self):
        return self.apiParas['proportion_list']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
