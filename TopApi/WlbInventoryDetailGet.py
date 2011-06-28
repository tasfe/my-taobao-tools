class WlbInventoryDetailGet(object):
    apiParas={'method':'taobao.wlb.inventory.detail.get'}
    def setInventoryTypeList(self,inventoryTypeList):
        self.apiParas['inventory_type_list']=inventoryTypeList
    def getInventoryTypeList(self):
        return self.apiParas['inventory_type_list']
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setStoreCode(self,storeCode):
        self.apiParas['store_code']=storeCode
    def getStoreCode(self):
        return self.apiParas['store_code']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
