# /usr/bin/python
# coding: utf-8
import os;

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options
from framework.utils import session
from framework.utils.WeixinUtils import WeixinMananger
from subsystem.WEB.handle.accountHandle import RechargeHandler
from subsystem.WEB.handle.bikeHandle import BikeCtrlHandler, BikeInfoHandler, NearIdleBikeHandler

from subsystem.WEB.handle.routerHandle import RouterHandler
from subsystem.WEB.handle.svcHandle import *
from subsystem.WEB.handle.userHandler import UserInfoHandler, CheckPhoneHandle, RegHandler, LoginHandler, \
    SendPhoneCodeHandle
from subsystem.WEB.handle.weixinServiceHandle import WeixinServiceHandle
from subsystem.WEB.service.bikeService import BikeService
from subsystem.WEB.service.sService import SService
from subsystem.WEB.service.userService import  UserService
define("port", default=8001, help="run on the given port", type=int)


class ZebraApplicatoin(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret="e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
            session_secret="3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
            session_timeout=12000,

            store_options={
                'redis_host': 'localhost',
                'redis_port': 6379,
                'redis_pass': '',
            },

            debug=True,
            login_url="/wx/u/login",
            template_path=os.path.join(os.path.dirname(__file__), "t"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),

        )

        handlers = [
            (r"/", RouterHandler),
            (r"", RouterHandler),

            # 用户信息管理
            (r"/wx/u/reg", RegHandler),
            (r"/wx/u/checkPhone/(\d{11})", CheckPhoneHandle),
            (r"/wx/u/info", UserInfoHandler),
            (r"/wx/u/login", LoginHandler),

            # 车管
            (r"/wx/b/info", BikeInfoHandler),
            (r"/wx/b/ctrl/(\w*)", BikeCtrlHandler),
            (r"/wx/b/search", NearIdleBikeHandler),

            # 服务
            (r"/wx/s/create", CreateSvcHandler),
            (r"/wx/s/finish", FinishSvcHandler),

            # 帐户管理
            (r"/wx/a/recharge", RechargeHandler),


            # 第三方服务
            (r"/wx/send/phoneCode", SendPhoneCodeHandle),

            # 微信服务
            (r"/wx/service/(.*)", WeixinServiceHandle)

        ]

        tornado.web.Application.__init__(self, handlers, **settings)
        self.session_manager = session.SessionManager(settings["session_secret"], settings["store_options"],
                                                      settings["session_timeout"])

        self.userService = UserService()
        self.bikeService = BikeService()
        self.sService = SService()

        self.weixinManager = WeixinMananger()


        # xsrf_cookies=True,


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = ZebraApplicatoin()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
