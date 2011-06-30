class WlbOrderscheduleruleQuery(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.orderschedulerule.query'}
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
