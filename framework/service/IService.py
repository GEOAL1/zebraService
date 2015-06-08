from subsystem.SM.server.dao.userDao import UserDao


class IService(object):
    def __init__(self):
        self.userDao = UserDao()
        pass
pass
