class WlbItemAuthorizationAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.item.authorization.add'}
    def setAuthorizeEndTime(self,authorizeEndTime):
        self.apiParas['authorize_end_time']=authorizeEndTime
    def getAuthorizeEndTime(self):
        return self.apiParas['authorize_end_time']
    def setAuthorizeStartTime(self,authorizeStartTime):
        self.apiParas['authorize_start_time']=authorizeStartTime
    def getAuthorizeStartTime(self):
        return self.apiParas['authorize_start_time']
    def setConsignUserId(self,consignUserId):
        self.apiParas['consign_user_id']=consignUserId
    def getConsignUserId(self):
        return self.apiParas['consign_user_id']
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setName(self,name):
        self.apiParas['name']=name
    def getName(self):
        return self.apiParas['name']
    def setQuantity(self,quantity):
        self.apiParas['quantity']=quantity
    def getQuantity(self):
        return self.apiParas['quantity']
    def setRuleCode(self,ruleCode):
        self.apiParas['rule_code']=ruleCode
    def getRuleCode(self):
        return self.apiParas['rule_code']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
