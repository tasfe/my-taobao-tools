class ItempropsGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.itemprops.get'}
    def setChildPath(self,childPath):
        self.apiParas['child_path']=childPath
    def getChildPath(self):
        return self.apiParas['child_path']
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
    def setIsColorProp(self,isColorProp):
        self.apiParas['is_color_prop']=isColorProp
    def getIsColorProp(self):
        return self.apiParas['is_color_prop']
    def setIsEnumProp(self,isEnumProp):
        self.apiParas['is_enum_prop']=isEnumProp
    def getIsEnumProp(self):
        return self.apiParas['is_enum_prop']
    def setIsInputProp(self,isInputProp):
        self.apiParas['is_input_prop']=isInputProp
    def getIsInputProp(self):
        return self.apiParas['is_input_prop']
    def setIsItemProp(self,isItemProp):
        self.apiParas['is_item_prop']=isItemProp
    def getIsItemProp(self):
        return self.apiParas['is_item_prop']
    def setIsKeyProp(self,isKeyProp):
        self.apiParas['is_key_prop']=isKeyProp
    def getIsKeyProp(self):
        return self.apiParas['is_key_prop']
    def setIsSaleProp(self,isSaleProp):
        self.apiParas['is_sale_prop']=isSaleProp
    def getIsSaleProp(self):
        return self.apiParas['is_sale_prop']
    def setParentPid(self,parentPid):
        self.apiParas['parent_pid']=parentPid
    def getParentPid(self):
        return self.apiParas['parent_pid']
    def setPid(self,pid):
        self.apiParas['pid']=pid
    def getPid(self):
        return self.apiParas['pid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
