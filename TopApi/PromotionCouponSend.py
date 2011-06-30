class PromotionCouponSend(object):
    def __init__(self):
        self.apiParas={'method':'taobao.promotion.coupon.send'}
    def setBuyerNick(self,buyerNick):
        self.apiParas['buyer_nick']=buyerNick
    def getBuyerNick(self):
        return self.apiParas['buyer_nick']
    def setCouponId(self,couponId):
        self.apiParas['coupon_id']=couponId
    def getCouponId(self):
        return self.apiParas['coupon_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
