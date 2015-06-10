# /usr/bin/python
# coding: utf-8
import base64
import json
import logging
import random
import tornado
from tornado.web import authenticated
from tornado import gen
from framework.error.zebraError import ZebraError, InputArgsError, SendMessageApiError, ValidateCodeError, \
    SamePasswordError, ExistedPhoneError
from framework.protocol.jsonTemplate import JsonTemplate
from framework.utils.Constants import SessionUserID
from framework.utils.messageUtils import MessageUtile
from subsystem.WEB.handle.baseHandle import BaseHandler
from subsystem.WEB.utiles.restTemplate import RestTemplate

log = logging.getLogger("userInfoHandle")


class UserInfoHandler(BaseHandler):
    @authenticated
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        result = ""
        try:
            user_id = self.session[SessionUserID]
            body = self.application.userService.detailUserInfo(user_id)
            result = RestTemplate.newJsonRes().setBody(body)
        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            logging.exception(e)
            result = RestTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())


log = logging.getLogger("regHandler")


class RegHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        result = ""
        try:
            phone, password = self.argCheck()
            user_id = self.application.userService.register(phone, password)
            self.session[SessionUserID] = str(user_id)
            self.session.save();
            result = RestTemplate.newJsonRes()

        except ZebraError as e:
            result = RestTemplate.newZebraErrorRes(e)
        except Exception as e:
            log.error(e)
            result = RestTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())

    def argCheck(self):
        try:
            password = self.get_argument("password")
            retryPassword = self.get_argument("confirmPassword")
            phone = self.get_argument("ph")
            # mcode1 = self.get_argument("confirmCode")
            # mcode2 = self.session["confirmCode"]
            mcode1 = 123456;
            mcode2 = 123456;
        except:
            raise InputArgsError()

        if mcode2 is None or mcode1 != mcode2:
            raise ValidateCodeError()

        if password != retryPassword:
            raise SamePasswordError()
        phone = base64.decodestring(phone)
        return phone, password


class CheckPhoneHandle(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, input):
        x = yield self.check_phone(input)
        self.write(x)
        self.finish()

    @tornado.gen.coroutine
    def check_phone(self, phone):
        try:
            is_exist = self.application.userService.checkIsExistedPhone(phone)
            if (is_exist):
                raise ExistedPhoneError()
            else:
                result = RestTemplate.newJsonRes()
        except ZebraError as e:
            result = RestTemplate.newZebraErrorRes(e)
        except Exception as e:
            log.error(e)
            result = RestTemplate.newErrorJsonRes().setErrMsg(e)
        finally:
            raise gen.Return(result.toJson())


class SendPhoneCodeHandle(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        x = yield self.get_result()
        self.write(x)
        self.finish()

    def get_result(self):
        try:
            try:
                phone = self.get_argument("ph")
            except Exception as e:
                raise InputArgsError()
            code = random.randrange(100000, 999999)
            code = 123456
            resp = MessageUtile.sendValidCode(phone, code)
            body = json.loads(resp.body)

            if (body["error_code"] > 0):
                raise SendMessageApiError()
            self.session["confirmCode"] = '%s' % code
            self.session.save();
            result = JsonTemplate.newJsonRes()
        except ZebraError as e:
            result = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            result = JsonTemplate.newErrorJsonRes().setErrMsg(e.message)
        finally:
            raise gen.Return(result.toJson())


class LoginHandler(BaseHandler):
    def get(self):
        # 判断是否为微信用户，如果是，则存SESSION，和COOKIE后，直接重定向到主页，否则重定向到LOGIN页
        self.redirect("/static/login.html")

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        # 验证用户名和密码dd
        result = yield self.get_result()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        ret = ""
        try:
            try:
                phone = self.get_argument("un");
                password = self.get_argument("pw");
                phone = base64.decodestring(phone)
            except Exception as e:
                raise InputArgsError();

            user = self.application.userService.login(phone, password)

            self.session[SessionUserID] = user.uid;
            self.session.save()
            ret = RestTemplate.newJsonRes()

        except ZebraError as e:
            ret = RestTemplate.newZebraErrorRes(e)
        except Exception as e:
            log.error(e)
            ret = RestTemplate.newErrorJsonRes().setErrMsg("服务器忙，请稍候再试");
        raise gen.Return(ret.toJson())

