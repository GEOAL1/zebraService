# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25
import tornado
from tornado.web import authenticated;
from tornado import gen
from framework.utils.Constants import SessionUserID
from subsystem.WEB.handle.baseHandle import BaseHandler


class RouterHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        url = yield self.get_result()
        self.redirect(url)

    @tornado.gen.coroutine
    def get_result(self):
        try:
            url = "/static/login.html"
            user_id = self.session[SessionUserID]
            url = "/static/panel.html"
        except Exception as e:
            pass
        finally:
            raise gen.Return(url)
