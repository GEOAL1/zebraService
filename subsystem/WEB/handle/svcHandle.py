# /usr/bin/python
# coding: utf-8
import logging
from framework.utils.Constants import SessionUserID

log = logging.getLogger("serviceHandle")
import logging
import tornado
from tornado.web import authenticated
from tornado import gen

# /wx/b/ctrl/cmd
from framework.error.zebraError import InputArgsError, ZebraError, BikeNotFoundError
from subsystem.WEB.handle.baseHandle import BaseHandler
from subsystem.WEB.utiles.restTemplate import RestTemplate


class CreateSvcHandler(BaseHandler):
    @authenticated
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        result = yield self.get_result()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                bid = self.get_argument("bid")
                uid = self.session[SessionUserID]
            except Exception as e:
                raise InputArgsError()

            sid = self.application.sService.createService(uid, bid)

            ret = RestTemplate.newJsonRes().setErrMsg("服务建立成功 服务编号[%d]" % (sid))
        except ZebraError as e:
            ret = RestTemplate.newZebraErrorRes(e)
        except Exception as e:
            log.error(e)
            ret = RestTemplate.newErrorJsonRes().setErrMsg(e.message);
        raise gen.Return(ret.toJson())


class FinishSvcHandler(BaseHandler):
    @authenticated
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        result = yield self.get_result()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def get_result(self):
        try:
            try:
                sid = self.get_argument("sid")
                uid = self.session[SessionUserID]
            except Exception as e:
                raise InputArgsError()

            finishInfo = self.application.sService.finishService(uid, sid)

            ret = RestTemplate.newJsonRes().setErrMsg(finishInfo)
        except ZebraError as e:
            ret = RestTemplate.newZebraErrorRes(e)
        except Exception as e:
            log.error(e)
            ret = RestTemplate.newErrorJsonRes().setErrMsg(e.message);
        raise gen.Return(ret.toJson())
