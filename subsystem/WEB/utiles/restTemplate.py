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
    elif isinstance(obj,Decimal):
        return float(obj)
    else:
        raise TypeError('%r is not JSON serializable' % obj)


class RestTemplate:
    def __init__(self):
        self.errorCode = ErrorCode.success
        pass

    errorCode = ErrorCode.success
    e = ""
    body = None;

    @staticmethod
    def newJsonRes():
        return RestTemplate()

    @staticmethod
    def newErrorJsonRes():
        return RestTemplate().setErrorCode(ErrorCode.error)

    @staticmethod
    def newZebraErrorRes(zebError):
        return RestTemplate().setErrorCode(zebError.errCode).setErrMsg(zebError.errMsg)

    def setBody(self, body):
        self.body = body
        return self;

    def setErrMsg(self, msg):
        self.errorMeg = msg;
        return self;

    def setErrorCode(self, code):
        self.errorCode = code;
        return self;

    def toJson(self):
        return json.dumps(self.__dict__,default=_default)
