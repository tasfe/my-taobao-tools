class WangwangEserviceOnlinetimeGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wangwang.eservice.onlinetime.get'}
    def setEndDate(self,endDate):
        self.apiParas['end_date']=endDate
    def getEndDate(self):
        return self.apiParas['end_date']
    def setServiceStaffId(self,serviceStaffId):
        self.apiParas['service_staff_id']=serviceStaffId
    def getServiceStaffId(self):
        return self.apiParas['service_staff_id']
    def setStartDate(self,startDate):
        self.apiParas['start_date']=startDate
    def getStartDate(self):
        return self.apiParas['start_date']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
