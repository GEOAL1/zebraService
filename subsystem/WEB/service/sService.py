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
    def __init__(self, sm=SMService(), cm=CMService(), am=AMService(), dm=DMService()):
        self.sm = sm;
        self.cm = cm;
        self.am = am;
        self.dm = dm;

    def createService(self, uid, bid):
        # 查询该用户帐户是否可提供服务
        self.sm.apiCheckIsDebts(ReqUser(uid))

        # 查询该车辆是否能提供服务
        self.dm.apiCheckBIkeIsServicable(ReqBikeInfo(bid))

        # 创建服务ID
        serverInfo = self.sm.apiCreateService(ReqCreateService(uid, bid))
        # serverInfo = {"sid": 123456, "uid": ReqCreateService.uid, "bid": ReqCreateService.bid}

        # 通知车管对应的车辆的服务编号及相关信息
        self.dm.apiSetBikeToService(serverInfo)

        # 通知计费模块开始计费
        self.cm.apiStartCharging(serverInfo)

        return serverInfo.sid
        pass

    def finishService(self, uid, sid):
        # 查询服务信息，栓查该用户对此服务的有效性
        s = self.sm.apiGetServiceByUidAndSID(uid, sid)

        # 通知计费模块停止计费，返回本次消费金额信息
        costInfo = self.cm.apiStopCharging(s)
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
