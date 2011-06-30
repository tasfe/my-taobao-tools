class PictureGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.picture.get'}
    def setDeleted(self,deleted):
        self.apiParas['deleted']=deleted
    def getDeleted(self):
        return self.apiParas['deleted']
    def setEndDate(self,endDate):
        self.apiParas['end_date']=endDate
    def getEndDate(self):
        return self.apiParas['end_date']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setModifiedTime(self,modifiedTime):
        self.apiParas['modified_time']=modifiedTime
    def getModifiedTime(self):
        return self.apiParas['modified_time']
    def setOrderBy(self,orderBy):
        self.apiParas['order_by']=orderBy
    def getOrderBy(self):
        return self.apiParas['order_by']
    def setPageNo(self,pageNo):
        self.apiParas['page_no']=pageNo
    def getPageNo(self):
        return self.apiParas['page_no']
    def setPageSize(self,pageSize):
        self.apiParas['page_size']=pageSize
    def getPageSize(self):
        return self.apiParas['page_size']
    def setPictureCategoryId(self,pictureCategoryId):
        self.apiParas['picture_category_id']=pictureCategoryId
    def getPictureCategoryId(self):
        return self.apiParas['picture_category_id']
    def setPictureId(self,pictureId):
        self.apiParas['picture_id']=pictureId
    def getPictureId(self):
        return self.apiParas['picture_id']
    def setStartDate(self,startDate):
        self.apiParas['start_date']=startDate
    def getStartDate(self):
        return self.apiParas['start_date']
    def setTitle(self,title):
        self.apiParas['title']=title
    def getTitle(self):
        return self.apiParas['title']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
