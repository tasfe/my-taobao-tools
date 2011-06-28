class PromotionMembersGet(object):
    apiParas={'method':'taobao.promotion.members.get'}
    def setBuyerNick(self,buyerNick):
        self.apiParas['buyer_nick']=buyerNick
    def getBuyerNick(self):
        return self.apiParas['buyer_nick']
    def setCurrentPage(self,currentPage):
        self.apiParas['current_page']=currentPage
    def getCurrentPage(self):
        return self.apiParas['current_page']
    def setGrade(self,grade):
        self.apiParas['grade']=grade
    def getGrade(self):
        return self.apiParas['grade']
    def setMaxTradeAmoun(self,maxTradeAmoun):
        self.apiParas['max_trade_amoun']=maxTradeAmoun
    def getMaxTradeAmoun(self):
        return self.apiParas['max_trade_amoun']
    def setMaxTradeCount(self,maxTradeCount):
        self.apiParas['max_trade_count']=maxTradeCount
    def getMaxTradeCount(self):
        return self.apiParas['max_trade_count']
    def setMinTradeAmount(self,minTradeAmount):
        self.apiParas['min_trade_amount']=minTradeAmount
    def getMinTradeAmount(self):
        return self.apiParas['min_trade_amount']
    def setMinTradeCount(self,minTradeCount):
        self.apiParas['min_trade_count']=minTradeCount
    def getMinTradeCount(self):
        return self.apiParas['min_trade_count']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
