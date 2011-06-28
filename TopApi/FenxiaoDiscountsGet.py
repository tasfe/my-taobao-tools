class FenxiaoDiscountsGet(object):
    apiParas={'method':'taobao.fenxiao.discounts.get'}
    def setDiscountId(self,discountId):
        self.apiParas['discount_id']=discountId
    def getDiscountId(self):
        return self.apiParas['discount_id']
    def setExtFields(self,extFields):
        self.apiParas['ext_fields']=extFields
    def getExtFields(self):
        return self.apiParas['ext_fields']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
