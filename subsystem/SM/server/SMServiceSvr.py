# /usr/bin/python
# coding: utf-8
import logging

import tornado
from tornado import httpserver

from tornado.options import define, options
from framework.serviceFm import ZebraServiceSvr

from subsystem.SM.server.handle.serviceHandle import ServiceHandler
from subsystem.SM.server.service.userService import UserService

define('debug', default=False, help='enable debug mode')
define('port', default=8020, help='run on this port', type=int)
define('address', default="127.0.0.1", help='run on this address', type=str) #记得写外网IP，要不客户端连接不上
define('zookeepers', default="127.0.0.1:2181", help='run on this zookeeper cloudy', type=str) #

log = logging.getLogger("SMServer")


class SMServer(ZebraServiceSvr):
    def __init__(self):
        super(SMServer, self).__init__(options.address, options.port, "SM", options.zookeepers) #SM这是服务名称，根椐自己的服务自已改

        settings = {
            'debug': options.debug,  #是否开启调试
            'gzip': False,             #是否启动GZIP压缩
            'autoescape': None,
            'xsrf_cookies': False,
        }

        # 注册句柄
        handlers = [
            (r"/service", ServiceHandler),  #服务句柄
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
