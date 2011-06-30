class ProductPropimgUpload(object):
    def __init__(self):
        self.apiParas={'method':'taobao.product.propimg.upload'}
    def setId(self,id):
        self.apiParas['id']=id
    def getId(self):
        return self.apiParas['id']
    def setImage(self,image):
        self.apiParas['image']=image
    def getImage(self):
        return self.apiParas['image']
    def setPosition(self,position):
        self.apiParas['position']=position
    def getPosition(self):
        return self.apiParas['position']
    def setProductId(self,productId):
        self.apiParas['product_id']=productId
    def getProductId(self):
        return self.apiParas['product_id']
    def setProps(self,props):
        self.apiParas['props']=props
    def getProps(self):
        return self.apiParas['props']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
