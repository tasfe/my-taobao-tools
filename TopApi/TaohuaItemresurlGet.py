class TaohuaItemresurlGet(object):
    apiParas={'method':'taobao.taohua.itemresurl.get'}
    def setFileType(self,fileType):
        self.apiParas['file_type']=fileType
    def getFileType(self):
        return self.apiParas['file_type']
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def setPosition(self,position):
        self.apiParas['position']=position
    def getPosition(self):
        return self.apiParas['position']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
