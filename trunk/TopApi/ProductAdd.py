class ProductAdd(object):
    apiParas={'method':'taobao.product.add'}
    def setBinds(self,binds):
        self.apiParas['binds']=binds
    def getBinds(self):
        return self.apiParas['binds']
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
    def setCustomerProps(self,customerProps):
        self.apiParas['customer_props']=customerProps
    def getCustomerProps(self):
        return self.apiParas['customer_props']
    def setDesc(self,desc):
        self.apiParas['desc']=desc
    def getDesc(self):
        return self.apiParas['desc']
    def setImage(self,image):
        self.apiParas['image']=image
    def getImage(self):
        return self.apiParas['image']
    def setMajor(self,major):
        self.apiParas['major']=major
    def getMajor(self):
        return self.apiParas['major']
    def setMarketTime(self,marketTime):
        self.apiParas['market_time']=marketTime
    def getMarketTime(self):
        return self.apiParas['market_time']
    def setName(self,name):
        self.apiParas['name']=name
    def getName(self):
        return self.apiParas['name']
    def setNativeUnkeyprops(self,nativeUnkeyprops):
        self.apiParas['native_unkeyprops']=nativeUnkeyprops
    def getNativeUnkeyprops(self):
        return self.apiParas['native_unkeyprops']
    def setOuterId(self,outerId):
        self.apiParas['outer_id']=outerId
    def getOuterId(self):
        return self.apiParas['outer_id']
    def setPrice(self,price):
        self.apiParas['price']=price
    def getPrice(self):
        return self.apiParas['price']
    def setPropertyAlias(self,propertyAlias):
        self.apiParas['property_alias']=propertyAlias
    def getPropertyAlias(self):
        return self.apiParas['property_alias']
    def setProps(self,props):
        self.apiParas['props']=props
    def getProps(self):
        return self.apiParas['props']
    def setSaleProps(self,saleProps):
        self.apiParas['sale_props']=saleProps
    def getSaleProps(self):
        return self.apiParas['sale_props']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
