# /usr/bin/python
# coding: utf-8
import logging

class RegisterForm(object):
    def __init__(self,userID, phone, password):
        self.phone = phone
        self.password = password
        self.userID = userID
        pass

    @staticmethod
    def createFromDict(dict):
        return RegisterForm(dict["userID"], dict["phone"], dict["password"])

class RespCheckPhone:
    def __init__(self,phone,isExistd):
        self.phone = phone
        self.isExisted = isExistd

    @staticmethod
    def createFromDict(dict):
        return RespCheckPhone(dict["phone"], dict["isExisted"])

class  ReqcheckPhone():
    def __init__(self,phone):
        self.phone = phone

    @staticmethod
    def createFromDict(dict):
        return ReqcheckPhone(dict["phone"])


class ReqLogin(object):
    def __init__(self, phone, password):
        self.phone = phone
        self.password = password

    pass

    @staticmethod
    def createFromDict(dict):
        return ReqLogin(dict["phone"], dict["password"])


class RespLogin(object):
    def __init__(self, uid):
        self.uid = uid

    pass

    @staticmethod
    def createFromDict(dict):
        return RespLogin(dict["uid"])


class ReqUser:
    def __init__(self, uid):
        self.uid = uid
    pass

    @staticmethod
    def createFromDict(dict):
        return ReqUser(dict["uid"])


class ReqNearBike(object):
    def __init__(self, lng, lat, distance):
        self.lng = lng;
        self.lat = lat;
        self.distance = distance;

    @staticmethod
    def createFromDict(dict):
        return ReqNearBike(dict["lng"], dict["lat"], dict["distance"])


class ReqBikeInfo(object):
    def __init__(self, bid):
        self.bid = bid;

    @staticmethod
    def createFromDict(dict):
        return ReqBikeInfo(dict["bid"])


class ReqCreateService(object):
    def __init__(self, uid, did):
        self.uid = uid
        self.did = did

    @staticmethod
    def createFromDict(dict):
        return ReqCreateService(dict["uid"], dict["did"])


class Account(object):
    def __init__(self, dict):
        self.__dict__ = dict


class User:
    def __init__(self, dict):
        self.__dict__ = dict


class UserInfo(object):
    def __init__(self, dict):
        self.__dict__ = dict


class UserState(object):
    def __init__(self, dict):
        self.__dict__ = dict


class RespUserDetail:
    def __init__(self, dict):
        self.__dict__ = dict


class UserFullInfo(object):
    def __init__(self, dict):
        self.__dict__.update(dict)
    pass


class RespNearBike(object):
    def __init__(self, dict):
        self.__dict__.update(dict)

    pass

class RespAccIdAlloc(object):
    def __init__(self, uid):
        self.uid = uid

    pass

    @staticmethod
    def createFromDict(dict):
        return RespAccIdAlloc(dict["uid"])


class Svc():
    def __init__(self, sid=0, uid=0, did=0, s_state=0, mileage=0, start_time=0, end_time=0):
        self.sid = sid;
        self.s_state = s_state;
        self.uid = uid;
        self.mileage = mileage;
        self.start_time = start_time;
        self.end_time = end_time
        self.did = did;

    @staticmethod
    def createFromDict(dict):
        return Svc(dict["sid"], dict["s_state"], dict["uid"], dict["did"],
                   dict["mileage"], dict["start_time"], dict["end_time"])


    
class ReqAccount():
    def __init__(self, uid):
        self.uid = uid

    pass

    @staticmethod
    def createFromDict(dict):
        return ReqAccount(dict["uid"])
    
class RespAccDetail:
    def __init__(self, dict):
        self.__dict__ = dict