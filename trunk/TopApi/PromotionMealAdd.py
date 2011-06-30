class PromotionMealAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.promotion.meal.add'}
    def setItemList(self,itemList):
        self.apiParas['item_list']=itemList
    def getItemList(self):
        return self.apiParas['item_list']
    def setMealMemo(self,mealMemo):
        self.apiParas['meal_memo']=mealMemo
    def getMealMemo(self):
        return self.apiParas['meal_memo']
    def setMealName(self,mealName):
        self.apiParas['meal_name']=mealName
    def getMealName(self):
        return self.apiParas['meal_name']
    def setMealPrice(self,mealPrice):
        self.apiParas['meal_price']=mealPrice
    def getMealPrice(self):
        return self.apiParas['meal_price']
    def setPostageId(self,postageId):
        self.apiParas['postage_id']=postageId
    def getPostageId(self):
        return self.apiParas['postage_id']
    def setTypePostage(self,typePostage):
        self.apiParas['type_postage']=typePostage
    def getTypePostage(self):
        return self.apiParas['type_postage']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
