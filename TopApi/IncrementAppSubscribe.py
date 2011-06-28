class IncrementAppSubscribe(object):
    apiParas={'method':'taobao.increment.app.subscribe'}
    def setDuration(self,duration):
        self.apiParas['duration']=duration
    def getDuration(self):
        return self.apiParas['duration']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def setTopics(self,topics):
        self.apiParas['topics']=topics
    def getTopics(self):
        return self.apiParas['topics']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
