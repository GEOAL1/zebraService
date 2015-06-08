# /usr/bin/python
# coding: utf-8





class RegisterForm(object):
    def __init__(self, phone, password):
        self.phone = phone
        self.password = password
        pass

    @staticmethod
    def createFromDict(dict):
        return RegisterForm(dict["userID"], dict["phone"], dict["password"])
