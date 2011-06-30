class FenxiaoProductUpdate(object):
    def __init__(self):
        self.apiParas={'method':'taobao.fenxiao.product.update'}
    def setAlarmNumber(self,alarmNumber):
        self.apiParas['alarm_number']=alarmNumber
    def getAlarmNumber(self):
        return self.apiParas['alarm_number']
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
    def setPid(self,pid):
        self.apiParas['pid']=pid
    def getPid(self):
        return self.apiParas['pid']
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
    def setSkuCostPrices(self,skuCostPrices):
        self.apiParas['sku_cost_prices']=skuCostPrices
    def getSkuCostPrices(self):
        return self.apiParas['sku_cost_prices']
    def setSkuIds(self,skuIds):
        self.apiParas['sku_ids']=skuIds
    def getSkuIds(self):
        return self.apiParas['sku_ids']
    def setSkuOuterIds(self,skuOuterIds):
        self.apiParas['sku_outer_ids']=skuOuterIds
    def getSkuOuterIds(self):
        return self.apiParas['sku_outer_ids']
    def setSkuQuantitys(self,skuQuantitys):
        self.apiParas['sku_quantitys']=skuQuantitys
    def getSkuQuantitys(self):
        return self.apiParas['sku_quantitys']
    def setSkuStandardPrices(self,skuStandardPrices):
        self.apiParas['sku_standard_prices']=skuStandardPrices
    def getSkuStandardPrices(self):
        return self.apiParas['sku_standard_prices']
    def setStandardPrice(self,standardPrice):
        self.apiParas['standard_price']=standardPrice
    def getStandardPrice(self):
        return self.apiParas['standard_price']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
