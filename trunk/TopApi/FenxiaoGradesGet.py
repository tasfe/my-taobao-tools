class FenxiaoGradesGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.fenxiao.grades.get'}
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
