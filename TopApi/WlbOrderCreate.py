class WlbOrderCreate(object):
    apiParas={'method':'taobao.wlb.order.create'}
    def setAlipayNo(self,alipayNo):
        self.apiParas['alipay_no']=alipayNo
    def getAlipayNo(self):
        return self.apiParas['alipay_no']
    def setAttributes(self,attributes):
        self.apiParas['attributes']=attributes
    def getAttributes(self):
        return self.apiParas['attributes']
    def setBuyerNick(self,buyerNick):
        self.apiParas['buyer_nick']=buyerNick
    def getBuyerNick(self):
        return self.apiParas['buyer_nick']
    def setExpectEndTime(self,expectEndTime):
        self.apiParas['expect_end_time']=expectEndTime
    def getExpectEndTime(self):
        return self.apiParas['expect_end_time']
    def setExpectStartTime(self,expectStartTime):
        self.apiParas['expect_start_time']=expectStartTime
    def getExpectStartTime(self):
        return self.apiParas['expect_start_time']
    def setInvoinceInfo(self,invoinceInfo):
        self.apiParas['invoince_info']=invoinceInfo
    def getInvoinceInfo(self):
        return self.apiParas['invoince_info']
    def setIsFinished(self,isFinished):
        self.apiParas['is_finished']=isFinished
    def getIsFinished(self):
        return self.apiParas['is_finished']
    def setOrderCode(self,orderCode):
        self.apiParas['order_code']=orderCode
    def getOrderCode(self):
        return self.apiParas['order_code']
    def setOrderFlag(self,orderFlag):
        self.apiParas['order_flag']=orderFlag
    def getOrderFlag(self):
        return self.apiParas['order_flag']
    def setOrderItemList(self,orderItemList):
        self.apiParas['order_item_list']=orderItemList
    def getOrderItemList(self):
        return self.apiParas['order_item_list']
    def setOrderSubType(self,orderSubType):
        self.apiParas['order_sub_type']=orderSubType
    def getOrderSubType(self):
        return self.apiParas['order_sub_type']
    def setOrderType(self,orderType):
        self.apiParas['order_type']=orderType
    def getOrderType(self):
        return self.apiParas['order_type']
    def setOutBizCode(self,outBizCode):
        self.apiParas['out_biz_code']=outBizCode
    def getOutBizCode(self):
        return self.apiParas['out_biz_code']
    def setPackageCount(self,packageCount):
        self.apiParas['package_count']=packageCount
    def getPackageCount(self):
        return self.apiParas['package_count']
    def setPayableAmount(self,payableAmount):
        self.apiParas['payable_amount']=payableAmount
    def getPayableAmount(self):
        return self.apiParas['payable_amount']
    def setPrevOrderCode(self,prevOrderCode):
        self.apiParas['prev_order_code']=prevOrderCode
    def getPrevOrderCode(self):
        return self.apiParas['prev_order_code']
    def setReceiverInfo(self,receiverInfo):
        self.apiParas['receiver_info']=receiverInfo
    def getReceiverInfo(self):
        return self.apiParas['receiver_info']
    def setRemark(self,remark):
        self.apiParas['remark']=remark
    def getRemark(self):
        return self.apiParas['remark']
    def setScheduleEnd(self,scheduleEnd):
        self.apiParas['schedule_end']=scheduleEnd
    def getScheduleEnd(self):
        return self.apiParas['schedule_end']
    def setScheduleStart(self,scheduleStart):
        self.apiParas['schedule_start']=scheduleStart
    def getScheduleStart(self):
        return self.apiParas['schedule_start']
    def setScheduleType(self,scheduleType):
        self.apiParas['schedule_type']=scheduleType
    def getScheduleType(self):
        return self.apiParas['schedule_type']
    def setSenderInfo(self,senderInfo):
        self.apiParas['sender_info']=senderInfo
    def getSenderInfo(self):
        return self.apiParas['sender_info']
    def setServiceFee(self,serviceFee):
        self.apiParas['service_fee']=serviceFee
    def getServiceFee(self):
        return self.apiParas['service_fee']
    def setStoreCode(self,storeCode):
        self.apiParas['store_code']=storeCode
    def getStoreCode(self):
        return self.apiParas['store_code']
    def setTmsInfo(self,tmsInfo):
        self.apiParas['tms_info']=tmsInfo
    def getTmsInfo(self):
        return self.apiParas['tms_info']
    def setTmsOrderCode(self,tmsOrderCode):
        self.apiParas['tms_order_code']=tmsOrderCode
    def getTmsOrderCode(self):
        return self.apiParas['tms_order_code']
    def setTmsServiceCode(self,tmsServiceCode):
        self.apiParas['tms_service_code']=tmsServiceCode
    def getTmsServiceCode(self):
        return self.apiParas['tms_service_code']
    def setTotalAmount(self,totalAmount):
        self.apiParas['total_amount']=totalAmount
    def getTotalAmount(self):
        return self.apiParas['total_amount']
    def getApiMethodName(self):
        return self.apiParas['method']
    def getApiParas(self):
        return self.apiParas
