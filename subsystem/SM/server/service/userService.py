# /usr/bin/python
# coding: utf-8
from framework.error.zebraError import *
from framework.model import *
from framework.service.IService import IService
from subsystem.SM.server.dao.userDao import UserDao


class UserService():
    def __init__(self):
        self.userDao = UserDao()

    def register(self, registerForm):
        self.userDao.add(registerForm.userID,registerForm.phone,registerForm.password)
        pass
    pass

    def isExistedPhone(self,phone):
        if(self.userDao.getUserByPhone(phone) != None):
            return RespCheckPhone(phone, True)
        else:
            return RespCheckPhone(phone, False)
        pass

    def login(self, reqLogin):
        user = self.userDao.getUserByPhoneAndPassword(reqLogin.phone, reqLogin.password)
        if (user == None):
            raise UnameOrPasswordError()
        else:
            return RespLogin(user["uid"])

    def getUserDetailInfo(self, reqUser):
        userDetail = self.userDao.getUserAllInfoByUserID(reqUser.uid)
        if (userDetail == None):
            raise UserIsNotFoundedError()
        return RespUserDetail(userDetail)
