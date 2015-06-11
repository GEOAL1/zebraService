# /usr/bin/python
# coding: utf-8
import logging
import time
from framework.error.zebraError import *
from framework.model import *
from framework.protocol.commandCode import *
from framework.protocol.jsonTemplate import JsonTemplate
from framework.serviceFm import ZebraServiceCli


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s- %(filename)s:%(lineno)d"
)


class AMService(ZebraServiceCli):
    '''
        这是提供服务的客户端使用API，
        该类 继类的父类提供了通过ZK 寻找服务提供方的结口，目前可通过上层的
        get_master获得主服务地址，或通过get_slaver获得一个从服务地址，
        从目前的需求来将，直接用从地址

        提供的API
        以api开头，内部通过协议来请求，
        协议基本格式，参考
        请求
        {
          'body': {                   #请求的主体
            'phone': '15652750943',
            'password': 'password',
            'userID': '15111111'
          },
          'head': {
            'reqCode': 'REGISTER',  #请求的命令
            'timestamp': 'default', #时间
            'version': 'default',   #请求版本
            'uuid': 'default'       #安全校验
          }
        }

        返回
                {
          u'body': u'',                    返回主体
          u'head': {
            u'timestamp': u'default',
            u'respMsg': u'success',     返回一成功或出错信息
            u'version': u'default',
            u'uuid': u'default',
            u'respCode': 0              返回的结果码，一般0为成功，其它情况可参考模版下的ERROR类中的代码
          }
        }
    '''
    REQ_WEB_PATH = "/service"  #请求的服务的相对地址


    def __init__(self, zkAddrs="127.0.0.1:2181", name="AM"):
        '''
        :param zkAddrs:zk的地址，多个用，号隔开
        :param name: 服务的名称，要与服务器一致
        :return:    空
        '''
        ZebraServiceCli.__init__(self, name, zkAddrs)

    def apiAccIDAlloc(self):
        '''
            申请ACCT_ID,
            成功，返回ID
            失败 RAISE 异常和信息
        :return:
        '''
#         return int(time.time())
#         pass
        resp = self.ReqAndRespone(CMD_AM_ACCID_ALLOC, ReqUser(11), self.REQ_WEB_PATH)
        return RespAccIdAlloc(JsonTemplate.getRespBodyFromJson(resp))
        pass
        

    def apiGetAcctInfoByID(self, reqUser):
        '''
         获取生成返因ACCT对象，失败则抛出异常
        :param reqUser:
        :return: Account
        '''
#         return Account({"uid": reqUser.uid, "balance": 100, "point": 100})
#         pass
        resp = self.ReqAndRespone(CMD_AM_GETACCINFO_BYID, reqUser, self.REQ_WEB_PATH)
        return RespAccDetail(JsonTemplate.getRespBodyFromJson(resp))
        pass

if __name__ == '__main__':
    dm = AMService()
    print(dm.apiGetAcctInfoByID(ReqUser(100000007)))
    print(dm.apiAccIDAlloc().__dict__)
    time.sleep(1000)


