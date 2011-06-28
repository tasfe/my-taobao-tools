class WangwangEserviceGroupmemberGet(object):
    apiParas={'method':'taobao.wangwang.eservice.groupmember.get'}
    def setManagerId(self,managerId):
        self.apiParas['manager_id']=managerId
    def getManagerId(self):
        return self.apiParas['manager_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
