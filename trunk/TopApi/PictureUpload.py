class PictureUpload(object):
    apiParas={'method':'taobao.picture.upload'}
    def setImageInputTitle(self,imageInputTitle):
        self.apiParas['image_input_title']=imageInputTitle
    def getImageInputTitle(self):
        return self.apiParas['image_input_title']
    def setImg(self,img):
        self.apiParas['img']=img
    def getImg(self):
        return self.apiParas['img']
    def setPictureCategoryId(self,pictureCategoryId):
        self.apiParas['picture_category_id']=pictureCategoryId
    def getPictureCategoryId(self):
        return self.apiParas['picture_category_id']
    def setTitle(self,title):
        self.apiParas['title']=title
    def getTitle(self):
        return self.apiParas['title']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
