class PostageAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.postage.add'}
    def setEmsIncrease(self,emsIncrease):
        self.apiParas['ems_increase']=emsIncrease
    def getEmsIncrease(self):
        return self.apiParas['ems_increase']
    def setEmsPrice(self,emsPrice):
        self.apiParas['ems_price']=emsPrice
    def getEmsPrice(self):
        return self.apiParas['ems_price']
    def setExpressIncrease(self,expressIncrease):
        self.apiParas['express_increase']=expressIncrease
    def getExpressIncrease(self):
        return self.apiParas['express_increase']
    def setExpressPrice(self,expressPrice):
        self.apiParas['express_price']=expressPrice
    def getExpressPrice(self):
        return self.apiParas['express_price']
    def setMemo(self,memo):
        self.apiParas['memo']=memo
    def getMemo(self):
        return self.apiParas['memo']
    def setName(self,name):
        self.apiParas['name']=name
    def getName(self):
        return self.apiParas['name']
    def setPostIncrease(self,postIncrease):
        self.apiParas['post_increase']=postIncrease
    def getPostIncrease(self):
        return self.apiParas['post_increase']
    def setPostPrice(self,postPrice):
        self.apiParas['post_price']=postPrice
    def getPostPrice(self):
        return self.apiParas['post_price']
    def setPostageModeDests(self,postageModeDests):
        self.apiParas['postage_mode_dests']=postageModeDests
    def getPostageModeDests(self):
        return self.apiParas['postage_mode_dests']
    def setPostageModeIncreases(self,postageModeIncreases):
        self.apiParas['postage_mode_increases']=postageModeIncreases
    def getPostageModeIncreases(self):
        return self.apiParas['postage_mode_increases']
    def setPostageModePrices(self,postageModePrices):
        self.apiParas['postage_mode_prices']=postageModePrices
    def getPostageModePrices(self):
        return self.apiParas['postage_mode_prices']
    def setPostageModeTypes(self,postageModeTypes):
        self.apiParas['postage_mode_types']=postageModeTypes
    def getPostageModeTypes(self):
        return self.apiParas['postage_mode_types']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
