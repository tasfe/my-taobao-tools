class ProductPropimgDelete(object):
    def __init__(self):
        self.apiParas={'method':'taobao.product.propimg.delete'}
    def setId(self,id):
        self.apiParas['id']=id
    def getId(self):
        return self.apiParas['id']
    def setProductId(self,productId):
        self.apiParas['product_id']=productId
    def getProductId(self):
        return self.apiParas['product_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
