class WlbItemMapGetByExtentity(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.item.map.get.by.extentity'}
    def setExtEntityId(self,extEntityId):
        self.apiParas['ext_entity_id']=extEntityId
    def getExtEntityId(self):
        return self.apiParas['ext_entity_id']
    def setExtEntityType(self,extEntityType):
        self.apiParas['ext_entity_type']=extEntityType
    def getExtEntityType(self):
        return self.apiParas['ext_entity_type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
