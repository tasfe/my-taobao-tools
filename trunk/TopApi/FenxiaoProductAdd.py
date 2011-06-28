class FenxiaoProductAdd(object):
    apiParas={'method':'taobao.fenxiao.product.add'}
    def setAlarmNumber(self,alarmNumber):
        self.apiParas['alarm_number']=alarmNumber
    def getAlarmNumber(self):
        return self.apiParas['alarm_number']
    def setCategoryId(self,categoryId):
        self.apiParas['category_id']=categoryId
    def getCategoryId(self):
        return self.apiParas['category_id']
    def setCity(self,city):
        self.apiParas['city']=city
    def getCity(self):
        return self.apiParas['city']
    def setCostPrice(self,costPrice):
        self.apiParas['cost_price']=costPrice
    def getCostPrice(self):
        return self.apiParas['cost_price']
    def setDesc(self,desc):
        self.apiParas['desc']=desc
    def getDesc(self):
        return self.apiParas['desc']
    def setDiscountId(self,discountId):
        self.apiParas['discount_id']=discountId
    def getDiscountId(self):
        return self.apiParas['discount_id']
    def setHaveGuarantee(self,haveGuarantee):
        self.apiParas['have_guarantee']=haveGuarantee
    def getHaveGuarantee(self):
        return self.apiParas['have_guarantee']
    def setHaveInvoice(self,haveInvoice):
        self.apiParas['have_invoice']=haveInvoice
    def getHaveInvoice(self):
        return self.apiParas['have_invoice']
    def setName(self,name):
        self.apiParas['name']=name
    def getName(self):
        return self.apiParas['name']
    def setOuterId(self,outerId):
        self.apiParas['outer_id']=outerId
    def getOuterId(self):
        return self.apiParas['outer_id']
    def setPostageEms(self,postageEms):
        self.apiParas['postage_ems']=postageEms
    def getPostageEms(self):
        return self.apiParas['postage_ems']
    def setPostageFast(self,postageFast):
        self.apiParas['postage_fast']=postageFast
    def getPostageFast(self):
        return self.apiParas['postage_fast']
    def setPostageId(self,postageId):
        self.apiParas['postage_id']=postageId
    def getPostageId(self):
        return self.apiParas['postage_id']
    def setPostageOrdinary(self,postageOrdinary):
        self.apiParas['postage_ordinary']=postageOrdinary
    def getPostageOrdinary(self):
        return self.apiParas['postage_ordinary']
    def setPostageType(self,postageType):
        self.apiParas['postage_type']=postageType
    def getPostageType(self):
        return self.apiParas['postage_type']
    def setProductcatId(self,productcatId):
        self.apiParas['productcat_id']=productcatId
    def getProductcatId(self):
        return self.apiParas['productcat_id']
    def setProv(self,prov):
        self.apiParas['prov']=prov
    def getProv(self):
        return self.apiParas['prov']
    def setQuantity(self,quantity):
        self.apiParas['quantity']=quantity
    def getQuantity(self):
        return self.apiParas['quantity']
    def setRetailPriceHigh(self,retailPriceHigh):
        self.apiParas['retail_price_high']=retailPriceHigh
    def getRetailPriceHigh(self):
        return self.apiParas['retail_price_high']
    def setRetailPriceLow(self,retailPriceLow):
        self.apiParas['retail_price_low']=retailPriceLow
    def getRetailPriceLow(self):
        return self.apiParas['retail_price_low']
    def setStandardPrice(self,standardPrice):
        self.apiParas['standard_price']=standardPrice
    def getStandardPrice(self):
        return self.apiParas['standard_price']
    def setTradeType(self,tradeType):
        self.apiParas['trade_type']=tradeType
    def getTradeType(self):
        return self.apiParas['trade_type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
