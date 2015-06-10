# /usr/bin/python
# coding: utf-8
import logging
from framework.utils.Constants import *
from subsystem.WEB.handle.baseHandle import BaseHandler
import logging
import tornado
from tornado.web import authenticated
from tornado import gen
# /wx/b/ctrl/cmd
from framework.error.zebraError import *
from subsystem.WEB.handle.baseHandle import BaseHandler
from subsystem.WEB.utiles.restTemplate import RestTemplate

log = logging.getLogger("accountHandle")


class RechargeHandler(BaseHandler):
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

        pass
