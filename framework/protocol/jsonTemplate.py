# /usr/bin/python
# coding: utf-8
from datetime import datetime
from datetime import date
import json
from decimal import Decimal

from enum import Enum


class ErrorCode(Enum):
    success = 0
    error = 1


def _default(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        raise TypeError('%r is not JSON serializable' % obj)


JSON_S_VERSION = "version"
JSON_S_TIMESTAMP = "timestamp"
JSON_S_UUID = "uuid"
JSON_S_REQCODE = "reqCode"

JSON_S_RESPCODE = "respCode"
JSON_S_RSEPMSG = "respMsg"
JSON_S_BODY = "body"

class JsonTemplate:
    def __init__(self):
        self.body = {};
        self.head = {};
        pass

    @staticmethod
    def __newJson():
        req = JsonTemplate()
        req.head[JSON_S_VERSION] = "default"  #
        req.head[JSON_S_TIMESTAMP] = "default"
        req.head[JSON_S_UUID] = "default"
        return req

    @staticmethod
    def newJsonRequest(reqCode, body={}):
        req = JsonTemplate.__newJson()
        req.head[JSON_S_REQCODE] = reqCode
        req.body = body
        req.head = req.head
        return req

    @staticmethod
    def newJsonSuccessRes(respCode=0, respMsg="success", body=""):
        req = JsonTemplate.__newJson()
        req.head[JSON_S_RESPCODE] = respCode
        req.head[JSON_S_RSEPMSG] = respMsg
        req.body = body
        return req

    @staticmethod
    def newJsonErrorRes(respCode=-1, respMsg="undefine", body=""):
        req = JsonTemplate.__newJson()
        req.head[JSON_S_RESPCODE] = respCode
        req.head[JSON_S_RSEPMSG] = respMsg
        req.body = body
        return req

    def setBody(self, body):
        self.body = body
        return self

    @staticmethod
    def newZebraErrorRes(zebError):
        return JsonTemplate().newJsonErrorRes(zebError.errCode, zebError.errMsg)

    def toJson(self):
        return json.dumps(self.__dict__, default=_default)

    @staticmethod
    def getReqCodeFromJson(jsonReq):
        return jsonReq["head"][JSON_S_REQCODE]

    @staticmethod
    def getRespCodeFromJson(jsonResp):
        return jsonResp["head"][JSON_S_RESPCODE]

    @staticmethod
    def getRespMsgFromJson(jsonResp):
        return jsonResp["head"][JSON_S_RSEPMSG]

    @staticmethod
    def getRespBodyFromJson(jsonResp):
        return jsonResp[JSON_S_BODY]
