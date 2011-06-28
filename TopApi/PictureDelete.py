class PictureDelete(object):
    apiParas={'method':'taobao.picture.delete'}
    def setPictureIds(self,pictureIds):
        self.apiParas['picture_ids']=pictureIds
    def getPictureIds(self):
        return self.apiParas['picture_ids']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
