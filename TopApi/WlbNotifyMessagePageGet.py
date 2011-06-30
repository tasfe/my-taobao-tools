class WlbNotifyMessagePageGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.notify.message.page.get'}
    def setEndDate(self,endDate):
        self.apiParas['end_date']=endDate
    def getEndDate(self):
        return self.apiParas['end_date']
    def setMsgCode(self,msgCode):
        self.apiParas['msg_code']=msgCode
    def getMsgCode(self):
        return self.apiParas['msg_code']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setStartDate(self,startDate):
        self.apiParas['start_date']=startDate
    def getStartDate(self):
        return self.apiParas['start_date']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
