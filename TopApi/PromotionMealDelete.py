class PromotionMealDelete(object):
    def __init__(self):
        self.apiParas={'method':'taobao.promotion.meal.delete'}
    def setMealId(self,mealId):
        self.apiParas['meal_id']=mealId
    def getMealId(self):
        return self.apiParas['meal_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
