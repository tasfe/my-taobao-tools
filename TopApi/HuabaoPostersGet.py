class HuabaoPostersGet(object):
    apiParas={'method':'taobao.huabao.posters.get'}
    def setChannelId(self,channelId):
        self.apiParas['channel_id']=channelId
    def getChannelId(self):
        return self.apiParas['channel_id']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
