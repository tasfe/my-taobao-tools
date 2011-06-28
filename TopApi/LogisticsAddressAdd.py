class LogisticsAddressAdd(object):
    apiParas={'method':'taobao.logistics.address.add'}
    def setAddr(self,addr):
        self.apiParas['addr']=addr
    def getAddr(self):
        return self.apiParas['addr']
    def setCancelDef(self,cancelDef):
        self.apiParas['cancel_def']=cancelDef
    def getCancelDef(self):
        return self.apiParas['cancel_def']
    def setCity(self,city):
        self.apiParas['city']=city
    def getCity(self):
        return self.apiParas['city']
    def setContactName(self,contactName):
        self.apiParas['contact_name']=contactName
    def getContactName(self):
        return self.apiParas['contact_name']
    def setCountry(self,country):
        self.apiParas['country']=country
    def getCountry(self):
        return self.apiParas['country']
    def setGetDef(self,getDef):
        self.apiParas['get_def']=getDef
    def getGetDef(self):
        return self.apiParas['get_def']
    def setMemo(self,memo):
        self.apiParas['memo']=memo
    def getMemo(self):
        return self.apiParas['memo']
    def setMobilePhone(self,mobilePhone):
        self.apiParas['mobile_phone']=mobilePhone
    def getMobilePhone(self):
        return self.apiParas['mobile_phone']
    def setPhone(self,phone):
        self.apiParas['phone']=phone
    def getPhone(self):
        return self.apiParas['phone']
    def setProvince(self,province):
        self.apiParas['province']=province
    def getProvince(self):
        return self.apiParas['province']
    def setSellerCompany(self,sellerCompany):
        self.apiParas['seller_company']=sellerCompany
    def getSellerCompany(self):
        return self.apiParas['seller_company']
    def setSendDef(self,sendDef):
        self.apiParas['send_def']=sendDef
    def getSendDef(self):
        return self.apiParas['send_def']
    def setZipCode(self,zipCode):
        self.apiParas['zip_code']=zipCode
    def getZipCode(self):
        return self.apiParas['zip_code']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
