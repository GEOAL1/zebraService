# /usr/bin/python
# coding: utf-8
from framework.error.zebraError import *
from framework.service.IService import IService
from framework.model import RespAccIdAlloc, RespAccDetail
from subsystem.AM.server.dao.accountDao import AccountDao


class AccountService(IService):
    def __init__(self):
        self.accountDao = AccountDao()

    def accIdAlloc(self):
        account = self.accountDao.add()
        #根据实际数据库字段来定
        return RespAccIdAlloc(account)
        pass


    def getAccInfoById(self, reqAccount):
        accDetail = self.accountDao.getAccountInfoByID(reqAccount)
        if (accDetail == None):
            raise AccountIsNotFoundedError()
        return RespAccDetail(accDetail)
