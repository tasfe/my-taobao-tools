class FenxiaoDiscountAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.fenxiao.discount.add'}
    def setDiscountName(self,discountName):
        self.apiParas['discount_name']=discountName
    def getDiscountName(self):
        return self.apiParas['discount_name']
    def setDiscountTypes(self,discountTypes):
        self.apiParas['discount_types']=discountTypes
    def getDiscountTypes(self):
        return self.apiParas['discount_types']
    def setDiscountValues(self,discountValues):
        self.apiParas['discount_values']=discountValues
    def getDiscountValues(self):
        return self.apiParas['discount_values']
    def setTargetIds(self,targetIds):
        self.apiParas['target_ids']=targetIds
    def getTargetIds(self):
        return self.apiParas['target_ids']
    def setTargetTypes(self,targetTypes):
        self.apiParas['target_types']=targetTypes
    def getTargetTypes(self):
        return self.apiParas['target_types']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
