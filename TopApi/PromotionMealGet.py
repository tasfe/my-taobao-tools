class PromotionMealGet(object):
    apiParas={'method':'taobao.promotion.meal.get'}
    def setMealId(self,mealId):
        self.apiParas['meal_id']=mealId
    def getMealId(self):
        return self.apiParas['meal_id']
    def setStatus(self,status):
        self.apiParas['status']=status
    def getStatus(self):
        return self.apiParas['status']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
