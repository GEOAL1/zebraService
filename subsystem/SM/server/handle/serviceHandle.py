# /usr/bin/python
# coding: utf-8
import json

import tornado
import tornado.web

from tornado import gen

from framework.error.zebraError import *
from framework.model.request import RegisterForm, CMD_SM_REGISTER
from framework.protocol.jsonTemplate import JsonTemplate
from framework.model import *

log = logging.getLogger("serviceHandler")


class ServiceHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(ServiceHandler, self).__init__(application, request, **kwargs)
        '''
            请求的映射表
        '''
        self.reqMap = {
            CMD_SM_REGISTER: self.register
        }

    def get(self):
        self.write("aaa")
        pass

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        result = yield self.getResponse()
        self.write(result)
        self.finish()

    @tornado.gen.coroutine
    def getResponse(self):
        try:
            reqBody = json.loads(self.request.body)
            if not self.reqMap.has_key(JsonTemplate.getReqCodeFromJson(reqBody)):
                raise InvaildReqCodeError()
            ret = self.reqMap[JsonTemplate.getReqCodeFromJson(reqBody)](reqBody)
        except ZebraError as e:
            ret = JsonTemplate.newZebraErrorRes(e)
        except Exception as e:
            print e
            ret = JsonTemplate.newJsonErrorRes()
        raise gen.Return(ret.toJson())
        pass




    def register(self, req):
        object = self.application.userService.register(RegisterForm.createFromDict(req["body"]))
        return JsonTemplate.newJsonSuccessRes(body="")
