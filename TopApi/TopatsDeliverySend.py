class TopatsDeliverySend(object):
    apiParas={'method':'taobao.topats.delivery.send'}
    def setCompanyCodes(self,companyCodes):
        self.apiParas['company_codes']=companyCodes
    def getCompanyCodes(self):
        return self.apiParas['company_codes']
    def setMemos(self,memos):
        self.apiParas['memos']=memos
    def getMemos(self):
        return self.apiParas['memos']
    def setOrderTypes(self,orderTypes):
        self.apiParas['order_types']=orderTypes
    def getOrderTypes(self):
        return self.apiParas['order_types']
    def setOutSids(self,outSids):
        self.apiParas['out_sids']=outSids
    def getOutSids(self):
        return self.apiParas['out_sids']
    def setSellerAddress(self,sellerAddress):
        self.apiParas['seller_address']=sellerAddress
    def getSellerAddress(self):
        return self.apiParas['seller_address']
    def setSellerAreaId(self,sellerAreaId):
        self.apiParas['seller_area_id']=sellerAreaId
    def getSellerAreaId(self):
        return self.apiParas['seller_area_id']
    def setSellerMobile(self,sellerMobile):
        self.apiParas['seller_mobile']=sellerMobile
    def getSellerMobile(self):
        return self.apiParas['seller_mobile']
    def setSellerName(self,sellerName):
        self.apiParas['seller_name']=sellerName
    def getSellerName(self):
        return self.apiParas['seller_name']
    def setSellerPhone(self,sellerPhone):
        self.apiParas['seller_phone']=sellerPhone
    def getSellerPhone(self):
        return self.apiParas['seller_phone']
    def setSellerZip(self,sellerZip):
        self.apiParas['seller_zip']=sellerZip
    def getSellerZip(self):
        return self.apiParas['seller_zip']
    def setTids(self,tids):
        self.apiParas['tids']=tids
    def getTids(self):
        return self.apiParas['tids']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
