class TaohuaChildcatesGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.taohua.childcates.get'}
    def setCateId(self,cateId):
        self.apiParas['cate_id']=cateId
    def getCateId(self):
        return self.apiParas['cate_id']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
