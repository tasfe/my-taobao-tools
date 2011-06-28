class ItemPropimgUpload(object):
    apiParas={'method':'taobao.item.propimg.upload'}
    def setId(self,id):
        self.apiParas['id']=id
    def getId(self):
        return self.apiParas['id']
    def setImage(self,image):
        self.apiParas['image']=image
    def getImage(self):
        return self.apiParas['image']
    def setNumIid(self,numIid):
        self.apiParas['num_iid']=numIid
    def getNumIid(self):
        return self.apiParas['num_iid']
    def setPosition(self,position):
        self.apiParas['position']=position
    def getPosition(self):
        return self.apiParas['position']
    def setProperties(self,properties):
        self.apiParas['properties']=properties
    def getProperties(self):
        return self.apiParas['properties']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
