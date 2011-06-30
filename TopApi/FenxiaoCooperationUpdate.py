class FenxiaoCooperationUpdate(object):
    def __init__(self):
        self.apiParas={'method':'taobao.fenxiao.cooperation.update'}
    def setDistributorId(self,distributorId):
        self.apiParas['distributor_id']=distributorId
    def getDistributorId(self):
        return self.apiParas['distributor_id']
    def setGradeId(self,gradeId):
        self.apiParas['grade_id']=gradeId
    def getGradeId(self):
        return self.apiParas['grade_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
