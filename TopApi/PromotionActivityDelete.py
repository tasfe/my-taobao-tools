class PromotionActivityDelete(object):
    apiParas={'method':'taobao.promotion.activity.delete'}
    def setActivityId(self,activityId):
        self.apiParas['activity_id']=activityId
    def getActivityId(self):
        return self.apiParas['activity_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
