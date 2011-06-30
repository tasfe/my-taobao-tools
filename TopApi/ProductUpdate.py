class ProductUpdate(object):
    def __init__(self):
        self.apiParas={'method':'taobao.product.update'}
    def setBinds(self,binds):
        self.apiParas['binds']=binds
    def getBinds(self):
        return self.apiParas['binds']
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
    def setProductId(self,productId):
        self.apiParas['product_id']=productId
    def getProductId(self):
        return self.apiParas['product_id']
    def setSaleProps(self,saleProps):
        self.apiParas['sale_props']=saleProps
    def getSaleProps(self):
        return self.apiParas['sale_props']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
