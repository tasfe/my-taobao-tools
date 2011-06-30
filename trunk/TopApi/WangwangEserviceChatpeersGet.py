class WangwangEserviceChatpeersGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wangwang.eservice.chatpeers.get'}
    def setCharset(self,charset):
        self.apiParas['charset']=charset
    def getCharset(self):
        return self.apiParas['charset']
    def setChatId(self,chatId):
        self.apiParas['chat_id']=chatId
    def getChatId(self):
        return self.apiParas['chat_id']
    def setEndDate(self,endDate):
        self.apiParas['end_date']=endDate
    def getEndDate(self):
        return self.apiParas['end_date']
    def setStartDate(self,startDate):
        self.apiParas['start_date']=startDate
    def getStartDate(self):
        return self.apiParas['start_date']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
