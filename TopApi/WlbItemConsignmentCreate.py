class WlbItemConsignmentCreate(object):
    apiParas={'method':'taobao.wlb.item.consignment.create'}
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setNumber(self,number):
        self.apiParas['number']=number
    def getNumber(self):
        return self.apiParas['number']
    def setOwnerItemId(self,ownerItemId):
        self.apiParas['owner_item_id']=ownerItemId
    def getOwnerItemId(self):
        return self.apiParas['owner_item_id']
    def setOwnerUserId(self,ownerUserId):
        self.apiParas['owner_user_id']=ownerUserId
    def getOwnerUserId(self):
        return self.apiParas['owner_user_id']
    def setRuleId(self,ruleId):
        self.apiParas['rule_id']=ruleId
    def getRuleId(self):
        return self.apiParas['rule_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
