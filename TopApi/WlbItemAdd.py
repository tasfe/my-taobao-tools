class WlbItemAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.item.add'}
    def setColor(self,color):
        self.apiParas['color']=color
    def getColor(self):
        return self.apiParas['color']
    def setGoodsCat(self,goodsCat):
        self.apiParas['goods_cat']=goodsCat
    def getGoodsCat(self):
        return self.apiParas['goods_cat']
    def setHeight(self,height):
        self.apiParas['height']=height
    def getHeight(self):
        return self.apiParas['height']
    def setIsDangerous(self,isDangerous):
        self.apiParas['is_dangerous']=isDangerous
    def getIsDangerous(self):
        return self.apiParas['is_dangerous']
    def setIsFriable(self,isFriable):
        self.apiParas['is_friable']=isFriable
    def getIsFriable(self):
        return self.apiParas['is_friable']
    def setIsSku(self,isSku):
        self.apiParas['is_sku']=isSku
    def getIsSku(self):
        return self.apiParas['is_sku']
    def setItemCode(self,itemCode):
        self.apiParas['item_code']=itemCode
    def getItemCode(self):
        return self.apiParas['item_code']
    def setLength(self,length):
        self.apiParas['length']=length
    def getLength(self):
        return self.apiParas['length']
    def setName(self,name):
        self.apiParas['name']=name
    def getName(self):
        return self.apiParas['name']
    def setPackageMaterial(self,packageMaterial):
        self.apiParas['package_material']=packageMaterial
    def getPackageMaterial(self):
        return self.apiParas['package_material']
    def setPrice(self,price):
        self.apiParas['price']=price
    def getPrice(self):
        return self.apiParas['price']
    def setPricingCat(self,pricingCat):
        self.apiParas['pricing_cat']=pricingCat
    def getPricingCat(self):
        return self.apiParas['pricing_cat']
    def setProNameList(self,proNameList):
        self.apiParas['pro_name_list']=proNameList
    def getProNameList(self):
        return self.apiParas['pro_name_list']
    def setProValueList(self,proValueList):
        self.apiParas['pro_value_list']=proValueList
    def getProValueList(self):
        return self.apiParas['pro_value_list']
    def setRemark(self,remark):
        self.apiParas['remark']=remark
    def getRemark(self):
        return self.apiParas['remark']
    def setSupportBatch(self,supportBatch):
        self.apiParas['support_batch']=supportBatch
    def getSupportBatch(self):
        return self.apiParas['support_batch']
    def setTitle(self,title):
        self.apiParas['title']=title
    def getTitle(self):
        return self.apiParas['title']
    def setType(self,type):
        self.apiParas['type']=type
    def getType(self):
        return self.apiParas['type']
    def setVolume(self,volume):
        self.apiParas['volume']=volume
    def getVolume(self):
        return self.apiParas['volume']
    def setWeight(self,weight):
        self.apiParas['weight']=weight
    def getWeight(self):
        return self.apiParas['weight']
    def setWidth(self,width):
        self.apiParas['width']=width
    def getWidth(self):
        return self.apiParas['width']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
