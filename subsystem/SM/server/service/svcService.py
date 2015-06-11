# /usr/bin/python
# coding: utf-8
from framework.error.zebraError import *
from framework.model import *
from framework.service.IService import IService
from subsystem.SM.server.dao.svcDao import SvcDao
from subsystem.SM.server.dao.userDao import UserDao


class SvcService():
    def __init__(self):
        self.userDao = UserDao()
        self.svcDao = SvcDao()

    def createSvc(self, reqCreateService):
        return self.svcDao.createService(reqCreateService.uid, reqCreateService.did)
