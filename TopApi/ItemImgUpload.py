class ItemImgUpload(object):
    def __init__(self):
        self.apiParas={'method':'taobao.item.img.upload'}
    def setId(self,id):
        self.apiParas['id']=id
    def getId(self):
        return self.apiParas['id']
    def setImage(self,image):
        self.apiParas['image']=image
    def getImage(self):
        return self.apiParas['image']
    def setIsMajor(self,isMajor):
        self.apiParas['is_major']=isMajor
    def getIsMajor(self):
        return self.apiParas['is_major']
    def setNumIid(self,numIid):
        self.apiParas['num_iid']=numIid
    def getNumIid(self):
        return self.apiParas['num_iid']
    def setPosition(self,position):
        self.apiParas['position']=position
    def getPosition(self):
        return self.apiParas['position']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
