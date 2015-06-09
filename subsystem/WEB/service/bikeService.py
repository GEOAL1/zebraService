# /usr/bin/python
# coding: utf-8
import logging
from framework.model import RegisterForm, ReqLogin, ReqcheckPhone, ReqUser, UserFullInfo, \
    ReqNearBike, ReqBikeInfo
from subsystem.AM.amService import AMService
from subsystem.CM.cmService import CMService
from subsystem.DM.dmService import DMService
from subsystem.SM.smService import SMService

log = logging.getLogger("bikeService")


class BikeService():
    def __init__(self, sm=SMService(), cm=CMService(), am=AMService(), dm=DMService()):
        self.sm = sm;
        self.cm = cm;
        self.am = am;
        self.dm = dm;
        pass

    def getNearIdleBIke(self, lng, lat, distance):
        return self.dm.apiSearchBikeByDistance(ReqNearBike(lng, lat, distance))

    def getBikeInfo(self, bid):
        return self.dm.apiGetBikeInfo(ReqBikeInfo(bid))
