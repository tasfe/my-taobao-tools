class ProductsSearch(object):
    def __init__(self):
        self.apiParas={'method':'taobao.products.search'}
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setProps(self,props):
        self.apiParas['props']=props
    def getProps(self):
        return self.apiParas['props']
    def setQ(self,q):
        self.apiParas['q']=q
    def getQ(self):
        return self.apiParas['q']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def setVerticalMarket(self,verticalMarket):
        self.apiParas['vertical_market']=verticalMarket
    def getVerticalMarket(self):
        return self.apiParas['vertical_market']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
