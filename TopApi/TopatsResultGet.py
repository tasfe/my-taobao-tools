class TopatsResultGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.topats.result.get'}
    def setTaskId(self,taskId):
        self.apiParas['task_id']=taskId
    def getTaskId(self):
        return self.apiParas['task_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
