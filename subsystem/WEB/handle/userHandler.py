# /usr/bin/python
# coding: utf-8
import logging
import tornado
from tornado.web import authenticated
from tornado import gen
from framework.error.zebraError import ZebraError
from framework.protocol.jsonTemplate import JsonTemplate
from framework.utils.Constants import SessionUserID
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
