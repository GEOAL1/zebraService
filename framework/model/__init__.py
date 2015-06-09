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
