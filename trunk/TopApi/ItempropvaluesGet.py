class ItempropvaluesGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.itempropvalues.get'}
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
    def setDatetime(self,datetime):
        self.apiParas['datetime']=datetime
    def getDatetime(self):
        return self.apiParas['datetime']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setPvs(self,pvs):
        self.apiParas['pvs']=pvs
    def getPvs(self):
        return self.apiParas['pvs']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
