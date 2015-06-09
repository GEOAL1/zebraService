from subsystem.SM.server.dao.userDao import UserDao
from subsystem.AM.server.dao.accountDao import AccountDao


class IService(object):
    def __init__(self):
        self.userDao = UserDao()
        #待测试
#         self.accountDao = AccountDao()
        pass
pass
