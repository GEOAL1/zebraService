# /usr/bin/python
# coding: utf-8
import logging
from framework.model import RegisterForm, ReqLogin, ReqcheckPhone, ReqUser, UserFullInfo, \
    ReqNearBike, ReqBikeInfo
from subsystem.AM.amService import AMService
from subsystem.CM.cmService import CMService
from subsystem.DM.dmService import DMService
from subsystem.SM.smService import SMService
from subsystem.WEB.service.iWebService import IWebService

log = logging.getLogger("bikeService")


class BikeService(IWebService):

    def getNearIdleBIke(self, lng, lat, distance):
        return self.dm.apiSearchIdleBikeByDistance(ReqNearBike(lng, lat, distance))

    def getBikeInfo(self, bid):
        return self.dm.apiGetBikeInfo(ReqBikeInfo(bid))
