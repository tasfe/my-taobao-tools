class TaohuaItemcommentAdd(object):
    apiParas={'method':'taobao.taohua.itemcomment.add'}
    def setComment(self,comment):
        self.apiParas['comment']=comment
    def getComment(self):
        return self.apiParas['comment']
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
