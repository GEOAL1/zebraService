# /usr/bin/python
# coding: utf-8
import json

import tornado
import tornado.web

from tornado import gen

from framework.error.zebraError import *
from framework.protocol.commandCode import *
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
            CMD_SM_REGISTER: self.register,
            CMD_SM_CHECK_ISEXISTED_PHONE:self.isExistedPhone
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
            log.error(e)
            ret = JsonTemplate.newJsonErrorRes()
        raise gen.Return(ret.toJson())
        pass

    def register(self, req):
        self.application.userService.register(RegisterForm.createFromDict(req["body"]))
        return JsonTemplate.newJsonSuccessRes()

    def isExistedPhone(self,req):
        phone = JsonTemplate.getRespBodyFromJson(req)["phone"]
        isExist = self.application.userService.isExistedPhone(phone)
        resp = RespCheckPhone(phone,isExist)
        return JsonTemplate.newJsonSuccessRes().setBody(resp.__dict__)
