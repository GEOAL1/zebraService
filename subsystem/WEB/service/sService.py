# /usr/bin/python
# coding: utf-8
import logging
from framework.error.zebraError import UserIsDebtsError, BikeNoServicableError
from framework.model import *
from subsystem.AM.amService import AMService
from subsystem.CM.cmService import CMService
from subsystem.DM.dmService import DMService
from subsystem.SM.smService import SMService
from subsystem.WEB.service.iWebService import IWebService

log = logging.getLogger("sService")


class SService(IWebService):

    def createService(self, uid, bid):
        # 查询该用户帐户是否可提供服务
        if self.sm.apiCheckIsDebts(ReqUser):
            raise UserIsDebtsError()

        # 查询该车辆是否能提供服务
        if self.dm.apiCheckBIkeIsServicable(ReqBikeInfo(bid)):
            raise BikeNoServicableError()

        # 创建服务ID
        s = self.sm.apiCreateService(ReqCreateService(uid, bid))

        # 通知车管对应的车辆的服务编号及相关信息
        self.dm.apiSetBikeToService(s)

        # 通知计费模块开始计费
        self.cm.apiStartCharging(s)

        pass

    def finishService(self, uid, sid):
        # 查询服务信息，可该用户对此服务的有效性
        s = self.sm.apiGetServiceByUidAndSID(uid, sid)

        # 通知计费模块停止计费，返回本次消费金额信息
        costInfo = self.cm.apiStopChargint(s)
        # 通知车管模块结束本次服务，并得到本次服务的时间和里程
        self.dm.apiSetBikeToIdle(s)
        # 通过服务模块，结束本次服务
        self.sm.apiStopService(s)

        return "完成本次服务成功，共花费100元"

        pass

    def getServiceInfoByUidAndSID(self, uid, sid):
        # 向服务模块发起查询情求
        s = self.sm.apiGetServiceByUidAndSID(uid, sid)
        return s
        pass
