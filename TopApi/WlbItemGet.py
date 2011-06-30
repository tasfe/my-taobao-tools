class WlbItemGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.item.get'}
    def setItemId(self,itemId):
        self.apiParas['item_id']=itemId
    def getItemId(self):
        return self.apiParas['item_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
