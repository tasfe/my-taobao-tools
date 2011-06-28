class TraderateListAdd(object):
    apiParas={'method':'taobao.traderate.list.add'}
    def setAnony(self,anony):
        self.apiParas['anony']=anony
    def getAnony(self):
        return self.apiParas['anony']
    def setContent(self,content):
        self.apiParas['content']=content
    def getContent(self):
        return self.apiParas['content']
    def setOid(self,oid):
        self.apiParas['oid']=oid
    def getOid(self):
        return self.apiParas['oid']
    def setResult(self,result):
        self.apiParas['result']=result
    def getResult(self):
        return self.apiParas['result']
    def setRole(self,role):
        self.apiParas['role']=role
    def getRole(self):
        return self.apiParas['role']
    def setTid(self,tid):
        self.apiParas['tid']=tid
    def getTid(self):
        return self.apiParas['tid']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
