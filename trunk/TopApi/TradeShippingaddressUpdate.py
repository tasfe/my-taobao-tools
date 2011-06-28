class TradeShippingaddressUpdate(object):
    apiParas={'method':'taobao.trade.shippingaddress.update'}
    def setReceiverAddress(self,receiverAddress):
        self.apiParas['receiver_address']=receiverAddress
    def getReceiverAddress(self):
        return self.apiParas['receiver_address']
    def setReceiverCity(self,receiverCity):
        self.apiParas['receiver_city']=receiverCity
    def getReceiverCity(self):
        return self.apiParas['receiver_city']
    def setReceiverDistrict(self,receiverDistrict):
        self.apiParas['receiver_district']=receiverDistrict
    def getReceiverDistrict(self):
        return self.apiParas['receiver_district']
    def setReceiverMobile(self,receiverMobile):
        self.apiParas['receiver_mobile']=receiverMobile
    def getReceiverMobile(self):
        return self.apiParas['receiver_mobile']
    def setReceiverName(self,receiverName):
        self.apiParas['receiver_name']=receiverName
    def getReceiverName(self):
        return self.apiParas['receiver_name']
    def setReceiverPhone(self,receiverPhone):
        self.apiParas['receiver_phone']=receiverPhone
    def getReceiverPhone(self):
        return self.apiParas['receiver_phone']
    def setReceiverState(self,receiverState):
        self.apiParas['receiver_state']=receiverState
    def getReceiverState(self):
        return self.apiParas['receiver_state']
    def setReceiverZip(self,receiverZip):
        self.apiParas['receiver_zip']=receiverZip
    def getReceiverZip(self):
        return self.apiParas['receiver_zip']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
