# /usr/bin/python
# coding: utf-8

# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
import logging
import tornado
from tornado.web import authenticated
from tornado import gen




# /wx/b/ctrl/cmd
from framework.error.zebraError import InputArgsError, ZebraError, BikeNotFoundError
from subsystem.WEB.handle.baseHandle import BaseHandler
from subsystem.WEB.utiles.restTemplate import RestTemplate

log = logging.getLogger("bikeHandle")


class BikeCtrlHandler(BaseHandler):
    def get(self, cmd):
        try:
            bikeID = self.get_argument("bikeID")
            if cmd == "voice":
                result = RestTemplate.newJsonRes().setErrMsg(
                    "user : %s control bikeid %s voice" % (self.get_current_user(), bikeID)).toJson()
            if cmd == "light":
                result = RestTemplate.newJsonRes() \
                    .setErrMsg("user : %s control bikeid %s light" % (self.get_current_user(), bikeID)).toJson()
            if cmd == "lock":
                result = RestTemplate.newJsonRes() \
                    .setErrMsg("user : %s control bikeid %s lock" % (self.get_current_user(), bikeID)).toJson()
            if cmd == "unlock":
                result = RestTemplate.newJsonRes() \
                    .setErrMsg("user : %s control bikeid %s unlock" % (self.get_current_user(), bikeID)).toJson()
        except Exception as e:
            print e
            result = RestTemplate.newErrorJsonRes().setBody("error argument").toJson()
        self.write(result)
        pass


class NearBikeHandler(BaseHandler):
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
                lng = float(self.get_argument("lng"))
                lat = float(self.get_argument("lat"))
                distance = int(self.get_argument("distance"))
            except Exception as e:
                raise InputArgsError()

            bikeList = self.application.bikeService.getNearIdleBIke(lng, lat, distance)

            ret = RestTemplate.newJsonRes().setBody(bikeList)
        except ZebraError as e:
            ret = RestTemplate.newZebraErrorRes(e)
        except Exception as e:
            log.error(e)
            ret = RestTemplate.newErrorJsonRes().setErrMsg(e.message);
        raise gen.Return(ret.toJson())


class BikeInfoHandler(BaseHandler):
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
                bike_id = self.get_argument("bikeID")
            except Exception as e:
                raise InputArgsError()

            bike = self.application.bikeService.getBikeInfo(bike_id)

            ret = RestTemplate.newJsonRes().setBody(bike)
        except ZebraError as e:
            ret = RestTemplate.newZebraErrorRes(e)
        except Exception as e:
            ret = RestTemplate.newErrorJsonRes().setErrMsg(e.message);
        raise gen.Return(ret.toJson())
