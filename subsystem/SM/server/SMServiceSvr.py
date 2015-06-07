# /usr/bin/python
# coding: utf-8
import logging

import tornado
from tornado import httpserver

from tornado.options import define, options

from framework.ServiceFm import ZebraServiceSvr
from subsystem.SM.server.handle.serviceHandle import ServiceHandler
from subsystem.SM.server.service.userService import UserService

define('debug', default=False, help='enable debug mode')
define('port', default=8001, help='run on this port', type=int)
define('address', default="127.0.0.1", help='run on this address', type=str)
define('zookeepers', default="127.0.0.1:2181", help='run on this address', type=str)

log = logging.getLogger("SMServer")


class SMServer(ZebraServiceSvr):
    def __init__(self):
        super(SMServer, self).__init__(options.address, options.port, "SM", options.zookeepers)

        settings = {
            'debug': options.debug,
            'gzip': True,
            'autoescape': None,
            'xsrf_cookies': False,
        }

        # 注册句柄
        handlers = [
            (r"/service", ServiceHandler),
        ]

        # 注入服务
        self.userService = UserService()

        # 初始化WEB
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    application = SMServer()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
