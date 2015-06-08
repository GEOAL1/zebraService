#/usr/bin/python
#coding: utf-8
import logging
from framework.model import RegisterForm
from subsystem.AM.amService import AMService
from subsystem.CM.cmService import CMService
from subsystem.DM.dmService import DMService
from subsystem.SM.smService import SMService

log = logging.getLogger("userService")

class UserService():
    def __init__(self,sm=SMService(),cm=CMService(),am=AMService(),dm=DMService()):
        self.sm = sm;
        self.cm = cm;
        self.am = am;
        self.dm = dm;
        pass

    def register(self,phone,password):
        #请求计费ID
        acct_id = self.am.apiAccIDAlloc()

        #注册用户帐户和用户信息
        self.sm.apiRegister(RegisterForm(acct_id,phone,password))

        #成功返回 userid
        return acct_id

        #失败raise异常

    def checkIsExistedPhone(self,phone):
        is_exist = self.sm.apiCheckIsExistPhone(phone)
        return is_exist;
        pass