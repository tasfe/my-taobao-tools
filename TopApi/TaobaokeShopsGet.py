class TaobaokeShopsGet(object):
    apiParas={'method':'taobao.taobaoke.shops.get'}
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
    def setEndAuctioncount(self,endAuctioncount):
        self.apiParas['end_auctioncount']=endAuctioncount
    def getEndAuctioncount(self):
        return self.apiParas['end_auctioncount']
    def setEndCommissionrate(self,endCommissionrate):
        self.apiParas['end_commissionrate']=endCommissionrate
    def getEndCommissionrate(self):
        return self.apiParas['end_commissionrate']
    def setEndCredit(self,endCredit):
        self.apiParas['end_credit']=endCredit
    def getEndCredit(self):
        return self.apiParas['end_credit']
    def setEndTotalaction(self,endTotalaction):
        self.apiParas['end_totalaction']=endTotalaction
    def getEndTotalaction(self):
        return self.apiParas['end_totalaction']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setKeyword(self,keyword):
        self.apiParas['keyword']=keyword
    def getKeyword(self):
        return self.apiParas['keyword']
    def setNick(self,nick):
        self.apiParas['nick']=nick
    def getNick(self):
        return self.apiParas['nick']
    def setOnlyMall(self,onlyMall):
        self.apiParas['only_mall']=onlyMall
    def getOnlyMall(self):
        return self.apiParas['only_mall']
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
    def setStartAuctioncount(self,startAuctioncount):
        self.apiParas['start_auctioncount']=startAuctioncount
    def getStartAuctioncount(self):
        return self.apiParas['start_auctioncount']
    def setStartCommissionrate(self,startCommissionrate):
        self.apiParas['start_commissionrate']=startCommissionrate
    def getStartCommissionrate(self):
        return self.apiParas['start_commissionrate']
    def setStartCredit(self,startCredit):
        self.apiParas['start_credit']=startCredit
    def getStartCredit(self):
        return self.apiParas['start_credit']
    def setStartTotalaction(self,startTotalaction):
        self.apiParas['start_totalaction']=startTotalaction
    def getStartTotalaction(self):
        return self.apiParas['start_totalaction']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
