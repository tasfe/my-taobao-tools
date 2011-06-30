class HuabaoChannelGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.huabao.channel.get'}
    def setChannelId(self,channelId):
        self.apiParas['channel_id']=channelId
    def getChannelId(self):
        return self.apiParas['channel_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
