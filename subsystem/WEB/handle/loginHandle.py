# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
import base64
import logging
import tornado
from tornado import gen
from tornado.web import authenticated
from framework.error.zebraError import *
from framework.protocol.jsonTemplate import JsonTemplate
from framework.utils.Constants import SessionUserID
from subsystem.WEB.handle.baseHandle import BaseHandler
from subsystem.WEB.utiles.restTemplate import RestTemplate

log = logging.getLogger("loginHander")


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
