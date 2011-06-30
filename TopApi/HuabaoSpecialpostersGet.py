class HuabaoSpecialpostersGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.huabao.specialposters.get'}
    def setChannelIds(self,channelIds):
        self.apiParas['channel_ids']=channelIds
    def getChannelIds(self):
        return self.apiParas['channel_ids']
    def setNumber(self,number):
        self.apiParas['number']=number
    def getNumber(self):
        return self.apiParas['number']
    def setType(self,type):
        self.apiParas['type']=type
    def getType(self):
        return self.apiParas['type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
