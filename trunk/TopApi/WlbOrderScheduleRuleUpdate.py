class WlbOrderScheduleRuleUpdate(object):
    apiParas={'method':'taobao.wlb.order.schedule.rule.update'}
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
    def setScheduleRuleId(self,scheduleRuleId):
        self.apiParas['schedule_rule_id']=scheduleRuleId
    def getScheduleRuleId(self):
        return self.apiParas['schedule_rule_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
