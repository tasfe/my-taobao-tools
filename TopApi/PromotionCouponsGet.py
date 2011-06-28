class PromotionCouponsGet(object):
    apiParas={'method':'taobao.promotion.coupons.get'}
    def setCouponId(self,couponId):
        self.apiParas['coupon_id']=couponId
    def getCouponId(self):
        return self.apiParas['coupon_id']
    def setDenominations(self,denominations):
        self.apiParas['denominations']=denominations
    def getDenominations(self):
        return self.apiParas['denominations']
    def setEndTime(self,endTime):
        self.apiParas['end_time']=endTime
    def getEndTime(self):
        return self.apiParas['end_time']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
