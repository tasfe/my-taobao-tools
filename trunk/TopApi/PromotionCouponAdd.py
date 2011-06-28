class PromotionCouponAdd(object):
    apiParas={'method':'taobao.promotion.coupon.add'}
    def setCondition(self,condition):
        self.apiParas['condition']=condition
    def getCondition(self):
        return self.apiParas['condition']
    def setDenominations(self,denominations):
        self.apiParas['denominations']=denominations
    def getDenominations(self):
        return self.apiParas['denominations']
    def setEndTime(self,endTime):
        self.apiParas['end_time']=endTime
    def getEndTime(self):
        return self.apiParas['end_time']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
