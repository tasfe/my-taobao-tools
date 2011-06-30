class WlbOrderScheduleRuleAdd(object):
    def __init__(self):
        self.apiParas={'method':'taobao.wlb.order.schedule.rule.add'}
    def setBackupStoreId(self,backupStoreId):
        self.apiParas['backup_store_id']=backupStoreId
    def getBackupStoreId(self):
        return self.apiParas['backup_store_id']
    def setDefaultStoreId(self,defaultStoreId):
        self.apiParas['default_store_id']=defaultStoreId
    def getDefaultStoreId(self):
        return self.apiParas['default_store_id']
    def setOption(self,option):
        self.apiParas['option']=option
    def getOption(self):
        return self.apiParas['option']
    def setProvAreaIds(self,provAreaIds):
        self.apiParas['prov_area_ids']=provAreaIds
    def getProvAreaIds(self):
        return self.apiParas['prov_area_ids']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
