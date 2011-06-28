class PictureCategoryGet(object):
    apiParas={'method':'taobao.picture.category.get'}
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setParentId(self,parentId):
        self.apiParas['parent_id']=parentId
    def getParentId(self):
        return self.apiParas['parent_id']
    def setPictureCategoryId(self,pictureCategoryId):
        self.apiParas['picture_category_id']=pictureCategoryId
    def getPictureCategoryId(self):
        return self.apiParas['picture_category_id']
    def setPictureCategoryName(self,pictureCategoryName):
        self.apiParas['picture_category_name']=pictureCategoryName
    def getPictureCategoryName(self):
        return self.apiParas['picture_category_name']
    def setType(self,type):
        self.apiParas['type']=type
    def getType(self):
        return self.apiParas['type']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
