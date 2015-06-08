# /usr/bin/python
# coding: utf-8
import json
import logging
from os.path import basename
import zookeeper
import time

import tornado
from tornado import web
from tornado.httpclient import HTTPResponse
from zkclient import ZkClient, NodeChildrenListener
from tornado import httpclient

from framework.protocol.jsonTemplate import JsonTemplate

log = logging.getLogger("serviceFm")


class UpdateListener(NodeChildrenListener):
    '''
    监听服务器的结点变化
    '''

    def __init__(self, path, cb):
        super(UpdateListener, self).__init__(path)
        self.cb = cb

    def Update(self, children_name_list):
        self.cb()


pass


class ZebraServiceSvr(tornado.web.Application):
    ZEBRA_ROOT = "/zebra"
    '''
    提供一机制，能够提供一种服务，将本身存在信息注册在ZK上，解决单点故障问题，并提供发现其它结点的功能
    并自动选举MASTER
    服务提供一套客户端及服务器实现交类，子类可以对实现的具体服务进行扩展，交类提供一套交互机制
    '''

    def __init__(self, host, port, name="default", zkAddrs="127.0.0.1:2181"):
        self.isMaster = False
        self.host = host
        self.port = port
        self.name = name
        self.zkAddrs = zkAddrs
        self.zkSvcPath = "%s/%s" % (ZebraServiceSvr.ZEBRA_ROOT, name)
        self.zkSvcWorkPath = "%s/%s" % (self.zkSvcPath, "workers")
        self.__zkInit()
        self.__zkRegister()
        self.__refresh()
        self.seed = 0

    def __zkInit(self):
        '''
        完成初始化结点和连接ZK
        :return:
        '''
        self.zk = ZkClient(self.zkAddrs)
        nodes = (self.ZEBRA_ROOT, self.zkSvcPath, self.zkSvcWorkPath)

        for node in nodes:
            log.debug(node)

            if not self.zk.Exist(node, False):
                try:
                    self.zk.Create(node, "", 0)
                except Exception as e:
                    log.error("初化化ZK结点失败")
                    exit(1)
                    pass
        pass

    def __zkRegister(self):
        """
        完成注册功能
        :return:
        """
        self.path = self.zk.Create(self.zkSvcWorkPath + "/inst_", "%s:%d" % (self.host, self.port),
                                   zookeeper.EPHEMERAL | zookeeper.SEQUENCE)
        self.instName = basename(self.path)

        self.zk.AddNodeChildrenListener(UpdateListener(self.zkSvcWorkPath, self.__refresh))
        self.zk.GetChildren(self.zkSvcWorkPath, False)
        pass

    def __get_childs_value(self, path):
        childs = self.zk.GetChildren(path, False)
        res = [];
        for i in childs:
            addr = self.zk.Get("%s/%s" % (path, i), False)[0]
            res.append(addr)
            pass
        return res

    def __refresh(self):
        self.workerAddrs = self.__get_childs_value(self.zkSvcWorkPath)
        children = self.zk.GetChildren(self.zkSvcWorkPath, False)
        children.sort()

        # check if I'm master
        self.masters = children[:1]
        if self.instName in self.masters:
            self.isMaster = True
        else:
            self.isMaster = False
        self.masterAddr = self.zk.Get("%s/%s" % (self.zkSvcWorkPath, self.masters[0]), False)[0]
        log.info("I'm Master [%s]", self.isMaster)
        log.info("master addrs [%s] ", self.masterAddr)

    def getMaster(self):
        while True:
            if (self.masterAddr == None or len(self.masterAddr) == 0):
                time.sleep(2)
                continue
            break
        return self.masterAddr.split(":")

    def getSlave(self):
        while True:
            if (self.workerAddrs == None or len(self.workerAddrs) == 0):
                time.sleep(2)
                continue
            break
        self.seed = self.seed + 1
        index = self.seed % len(self.workerAddrs)
        return self.workerAddrs[index].split(":")


class ZebraServiceCli():
    ZEBRA_ROOT = "/zebra"
    '''
    服务提供一套客户端及服务器实现交类，子类可以对实现的具体服务进行扩展，交类提供一套交互机制
    '''

    def __init__(self, name="default", zkAddrs="127.0.0.1:2181"):
        self.zkAddrs = zkAddrs
        self.zkSvcPath = "%s/%s" % (ZebraServiceSvr.ZEBRA_ROOT, name)
        self.zkSvcWorkPath = "%s/%s" % (self.zkSvcPath, "workers")
        self.workerAddrs = ""
        self.seed = 1L  # 轮揗的种子

        self.__zkInit()
        self.__refresh()
        self.__register()
        self.masterAddrs = []
        self.masters = []

    def __zkInit(self):
        '''
        完成初始化结点和连接ZK
        :return:
        '''
        self.zk = ZkClient(self.zkAddrs)
        nodes = (self.ZEBRA_ROOT, self.zkSvcPath, self.zkSvcWorkPath)

        for node in nodes:
            log.debug(node)

            if not self.zk.Exist(node, False):
                try:
                    self.zk.Create(node, "", 0)
                except Exception as e:
                    log.error("初化化ZK结点失败")
                    exit(1)
                    pass
        pass

    def __register(self):
        '''
        注册WATCH,
        :return:
        '''
        self.zk.AddNodeChildrenListener(UpdateListener(self.zkSvcWorkPath, self.__refresh))
        self.zk.GetChildren(self.zkSvcWorkPath, True)

    def __refresh(self):
        try:
            self.workerAddrs = self.__get_childs_value(self.zkSvcWorkPath)
            children = self.zk.GetChildren(self.zkSvcWorkPath, False)
            children.sort()
            self.masters = children[:1]
            self.masterAddrs = self.zk.Get("%s/%s" % (self.zkSvcWorkPath, self.masters[0]), False)[0]
            log.info("master address [%s] ", self.masterAddrs)
        except:
            log.warn("refresh worker node error")
            pass

    def __get_childs_value(self, path):
        childs = self.zk.GetChildren(path, False)
        res = [];
        for i in childs:
            addr = self.zk.Get("%s/%s" % (path, i), False)[0]
            res.append(addr)
            pass
        return res

    def getMaster(self):
        while True:
            if (self.masterAddrs == None or len(self.masterAddrs) == 0):
                time.sleep(2)
                continue
            break
        return self.masterAddrs.split(":")

    def getSlave(self):
        while True:
            if (self.workerAddrs == None or len(self.workerAddrs) == 0):
                time.sleep(2)
                continue
            break
        self.seed = self.seed + 1
        index = self.seed % len(self.workerAddrs)
        return self.workerAddrs[index].split(":")

    def ReqAndRespone(self, requestCode, bodyObject, path):
        try:

            client = tornado.httpclient.HTTPClient()
            requestBody = JsonTemplate.newJsonRequest(requestCode, bodyObject.__dict__).toJson()
            host, port = self.getSlave()
            url = "http://%s:%s%s" % (host, port, path)
            http_request = tornado.httpclient.HTTPRequest(url=url, method='POST',
                                                          use_gzip=False, connect_timeout=8000, request_timeout=8000,
                                                          body=requestBody)
            resp = client.fetch(http_request)
            body =  json.loads(resp.body)
            return body
        except Exception as e:
            log.error(e.message)
            return JsonTemplate.newJsonErrorRes(-1, "请求异常")
        pass
