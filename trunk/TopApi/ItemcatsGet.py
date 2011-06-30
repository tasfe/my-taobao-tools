class ItemcatsGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.itemcats.get'}
    def setCids(self,cids):
        self.apiParas['cids']=cids
    def getCids(self):
        return self.apiParas['cids']
    def setDatetime(self,datetime):
        self.apiParas['datetime']=datetime
    def getDatetime(self):
        return self.apiParas['datetime']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setParentCid(self,parentCid):
        self.apiParas['parent_cid']=parentCid
    def getParentCid(self):
        return self.apiParas['parent_cid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
