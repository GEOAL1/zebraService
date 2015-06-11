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
            CMD_AM_ACCID_ALLOC: self.accIdAlloc,
            CMD_AM_GETACCINFO_BYID: self.getAccInfoById,
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
            ret = JsonTemplate.newJsonErrorRes(e)
        raise gen.Return(ret.toJson())
        pass
    
    def accIdAlloc(self,req):
        accID = self.application.accountService.accIdAlloc() 
        return JsonTemplate.newJsonSuccessRes().setBody(accID.__dict__)
        
    def getAccInfoById(self,req):
        #根据实际字段来定uid
        accID = JsonTemplate.getRespBodyFromJson(req)["uid"]
        accDetail = self.application.accountService.getAccInfoById(accID)
        return JsonTemplate.newJsonSuccessRes().setBody(accDetail.__dict__)
        
   
