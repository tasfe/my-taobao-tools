class ItemsGet(object):
    def __init__(self):
        self.apiParas={'method':'taobao.items.get'}
    def setCid(self,cid):
        self.apiParas['cid']=cid
    def getCid(self):
        return self.apiParas['cid']
    def setEndPrice(self,endPrice):
        self.apiParas['end_price']=endPrice
    def getEndPrice(self):
        return self.apiParas['end_price']
    def setEndScore(self,endScore):
        self.apiParas['end_score']=endScore
    def getEndScore(self):
        return self.apiParas['end_score']
    def setEndVolume(self,endVolume):
        self.apiParas['end_volume']=endVolume
    def getEndVolume(self):
        return self.apiParas['end_volume']
    def setFields(self,fields):
        self.apiParas['fields']=fields
    def getFields(self):
        return self.apiParas['fields']
    def setGenuineSecurity(self,genuineSecurity):
        self.apiParas['genuine_security']=genuineSecurity
    def getGenuineSecurity(self):
        return self.apiParas['genuine_security']
    def setIs3D(self,is3D):
        self.apiParas['is_3D']=is3D
    def getIs3D(self):
        return self.apiParas['is_3D']
    def setIsCod(self,isCod):
        self.apiParas['is_cod']=isCod
    def getIsCod(self):
        return self.apiParas['is_cod']
    def setIsMall(self,isMall):
        self.apiParas['is_mall']=isMall
    def getIsMall(self):
        return self.apiParas['is_mall']
    def setIsPrepay(self,isPrepay):
        self.apiParas['is_prepay']=isPrepay
    def getIsPrepay(self):
        return self.apiParas['is_prepay']
    def setLocationCity(self,locationCity):
        self.apiParas['location.city']=locationCity
    def getLocationCity(self):
        return self.apiParas['location.city']
    def setLocationState(self,locationState):
        self.apiParas['location.state']=locationState
    def getLocationState(self):
        return self.apiParas['location.state']
    def setNicks(self,nicks):
        self.apiParas['nicks']=nicks
    def getNicks(self):
        return self.apiParas['nicks']
    def setOneStation(self,oneStation):
        self.apiParas['one_station']=oneStation
    def getOneStation(self):
        return self.apiParas['one_station']
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
    def setPostFree(self,postFree):
        self.apiParas['post_free']=postFree
    def getPostFree(self):
        return self.apiParas['post_free']
    def setProductId(self,productId):
        self.apiParas['product_id']=productId
    def getProductId(self):
        return self.apiParas['product_id']
    def setPromotedService(self,promotedService):
        self.apiParas['promoted_service']=promotedService
    def getPromotedService(self):
        return self.apiParas['promoted_service']
    def setProps(self,props):
        self.apiParas['props']=props
    def getProps(self):
        return self.apiParas['props']
    def setQ(self,q):
        self.apiParas['q']=q
    def getQ(self):
        return self.apiParas['q']
    def setStartPrice(self,startPrice):
        self.apiParas['start_price']=startPrice
    def getStartPrice(self):
        return self.apiParas['start_price']
    def setStartScore(self,startScore):
        self.apiParas['start_score']=startScore
    def getStartScore(self):
        return self.apiParas['start_score']
    def setStartVolume(self,startVolume):
        self.apiParas['start_volume']=startVolume
    def getStartVolume(self):
        return self.apiParas['start_volume']
    def setStuffStatus(self,stuffStatus):
        self.apiParas['stuff_status']=stuffStatus
    def getStuffStatus(self):
        return self.apiParas['stuff_status']
    def setWwStatus(self,wwStatus):
        self.apiParas['ww_status']=wwStatus
    def getWwStatus(self):
        return self.apiParas['ww_status']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
