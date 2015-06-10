#/usr/bin/python
#coding: utf-8
import logging
from framework.model import RegisterForm, ReqLogin, ReqcheckPhone, ReqUser, UserFullInfo
from subsystem.AM.amService import AMService
from subsystem.CM.cmService import CMService
from subsystem.DM.dmService import DMService
from subsystem.SM.smService import SMService
from subsystem.WEB.service.iWebService import IWebService

log = logging.getLogger("userService")


class UserService(IWebService):

    def register(self,phone,password):
        #请求计费ID
        acct_id = self.am.apiAccIDAlloc()

        #注册用户帐户和用户信息
        self.sm.apiRegister(RegisterForm(acct_id,phone,password))

        #成功返回 userid
        return acct_id

        #失败raise异常

    def checkIsExistedPhone(self,phone):
        is_exist = self.sm.apiCheckIsExistPhone(ReqcheckPhone(phone))
        return is_exist;
        pass

    def login(self, phone, password):
        return self.sm.apiLogin(ReqLogin(phone, password))

    def detailUserInfo(self, user_id):
        # 请求帐户信息
        acct = self.am.apiGetAcctInfoByID(ReqUser(user_id))
        # 请求个人信息及个人状态
        userdetail = self.sm.apiGetUserDetailInfoByID(ReqUser(user_id))
        ret = dict(acct.__dict__, **userdetail.__dict__)
        return ret
