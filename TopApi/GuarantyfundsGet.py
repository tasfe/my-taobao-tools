class GuarantyfundsGet(object):
    apiParas={'method':'taobao.guarantyfunds.get'}
    def setBeginDate(self,beginDate):
        self.apiParas['begin_date']=beginDate
    def getBeginDate(self):
        return self.apiParas['begin_date']
    def setEndDate(self,endDate):
        self.apiParas['end_date']=endDate
    def getEndDate(self):
        return self.apiParas['end_date']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
