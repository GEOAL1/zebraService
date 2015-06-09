# /usr/bin/python
# coding: utf-8
from framework.error.zebraError import *
from framework.model import *
from framework.service.IService import IService


class UserService(IService):

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
