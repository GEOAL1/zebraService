#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
from subsystem.WEB.handle.baseHandle import BaseHandler


class DefaultHandler(BaseHandler):
    def get(self):
        self.write("get ok")
        None


    def post(self):
        self.write("post ok")
        None