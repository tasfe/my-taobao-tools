class PromotionActivityAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.promotion.activity.add'}
    def setCouponCount(self,couponCount):
        self.apiParas['coupon_count']=couponCount
    def getCouponCount(self):
        return self.apiParas['coupon_count']
    def setCouponId(self,couponId):
        self.apiParas['coupon_id']=couponId
    def getCouponId(self):
        return self.apiParas['coupon_id']
    def setPersonLimitCount(self,personLimitCount):
        self.apiParas['person_limit_count']=personLimitCount
    def getPersonLimitCount(self):
        return self.apiParas['person_limit_count']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
