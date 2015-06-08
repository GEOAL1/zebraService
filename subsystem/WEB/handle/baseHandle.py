#/usr/bin/python
#coding: utf-8
#Createtime 2015/5/25
import time

import tornado
from tornado.web import RequestHandler
from framework.utils import session
from framework.utils.Constants import SessionUserID


class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)
        self.session = session.Session(self.application.session_manager, self)
        try:
            if (int(time.time()) - self.session["create_time"] > 30):
                self.session.save()
        except:
            self.session.save()
            pass

    def get_current_user(self):
        return self.session.get(SessionUserID)

    def get_result(self):
        pass
