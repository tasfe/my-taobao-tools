class WlbItemUpdate(object):
    apiParas={'method':'taobao.wlb.item.update'}
    def setColor(self,color):
        self.apiParas['color']=color
    def getColor(self):
        return self.apiParas['color']
    def setDeletePropertyKeyList(self,deletePropertyKeyList):
        self.apiParas['delete_property_key_list']=deletePropertyKeyList
    def getDeletePropertyKeyList(self):
        return self.apiParas['delete_property_key_list']
    def setGoodsCat(self,goodsCat):
        self.apiParas['goods_cat']=goodsCat
    def getGoodsCat(self):
        return self.apiParas['goods_cat']
    def setHeight(self,height):
        self.apiParas['height']=height
    def getHeight(self):
        return self.apiParas['height']
    def setId(self,id):
        self.apiParas['id']=id
    def getId(self):
        return self.apiParas['id']
    def setIsDangerous(self,isDangerous):
        self.apiParas['is_dangerous']=isDangerous
    def getIsDangerous(self):
        return self.apiParas['is_dangerous']
    def setIsFriable(self,isFriable):
        self.apiParas['is_friable']=isFriable
    def getIsFriable(self):
        return self.apiParas['is_friable']
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
    def setPricingCat(self,pricingCat):
        self.apiParas['pricing_cat']=pricingCat
    def getPricingCat(self):
        return self.apiParas['pricing_cat']
    def setRemark(self,remark):
        self.apiParas['remark']=remark
    def getRemark(self):
        return self.apiParas['remark']
    def setTitle(self,title):
        self.apiParas['title']=title
    def getTitle(self):
        return self.apiParas['title']
    def setUpdatePropertyKeyList(self,updatePropertyKeyList):
        self.apiParas['update_property_key_list']=updatePropertyKeyList
    def getUpdatePropertyKeyList(self):
        return self.apiParas['update_property_key_list']
    def setUpdatePropertyValueList(self,updatePropertyValueList):
        self.apiParas['update_property_value_list']=updatePropertyValueList
    def getUpdatePropertyValueList(self):
        return self.apiParas['update_property_value_list']
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
