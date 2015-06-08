# /usr/bin/python
# coding: utf-8
from framework.service.IService import IService


class UserService(IService):

    def register(self, registerForm):
        self.userDao.add(registerForm.userID,registerForm.phone,registerForm.password)
        pass
    pass

    def isExistedPhone(self,phone):
        if(self.userDao.getUserByPhone(phone) != None):
            return True
        else:
            return False
        pass




