class ShopRemainshowcaseGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.shop.remainshowcase.get'}
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
