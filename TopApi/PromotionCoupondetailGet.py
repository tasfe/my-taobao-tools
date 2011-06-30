class PromotionCoupondetailGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.promotion.coupondetail.get'}
    def setBuyerNick(self,buyerNick):
        self.apiParas['buyer_nick']=buyerNick
    def getBuyerNick(self):
        return self.apiParas['buyer_nick']
    def setCouponId(self,couponId):
        self.apiParas['coupon_id']=couponId
    def getCouponId(self):
        return self.apiParas['coupon_id']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setState(self,state):
        self.apiParas['state']=state
    def getState(self):
        return self.apiParas['state']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
