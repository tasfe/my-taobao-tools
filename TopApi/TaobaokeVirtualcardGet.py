class TaobaokeVirtualcardGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.taobaoke.virtualcard.get'}
    def setArea(self,area):
        self.apiParas['area']=area
    def getArea(self):
        return self.apiParas['area']
    def setBizType(self,bizType):
        self.apiParas['biz_type']=bizType
    def getBizType(self):
        return self.apiParas['biz_type']
    def setCardType(self,cardType):
        self.apiParas['card_type']=cardType
    def getCardType(self):
        return self.apiParas['card_type']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setGameName(self,gameName):
        self.apiParas['game_name']=gameName
    def getGameName(self):
        return self.apiParas['game_name']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def setOperator(self,operator):
        self.apiParas['operator']=operator
    def getOperator(self):
        return self.apiParas['operator']
    def setOuterCode(self,outerCode):
        self.apiParas['outer_code']=outerCode
    def getOuterCode(self):
        return self.apiParas['outer_code']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setPid(self,pid):
        self.apiParas['pid']=pid
    def getPid(self):
        return self.apiParas['pid']
    def setPrice(self,price):
        self.apiParas['price']=price
    def getPrice(self):
        return self.apiParas['price']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
