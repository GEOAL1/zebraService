# /usr/bin/python
# coding: utf-8

from framework.ServiceFm import ZebraServiceCli
from framework.model.request import RegisterForm, CMD_SM_REGISTER


class SMServicCli(ZebraServiceCli):
    REQ_WEB_PATH = "/service"

    def __init__(self, zkAddrs="127.0.0.1:2181", name="SM"):
        ZebraServiceCli.__init__(self, name, zkAddrs)

    def register(self, registerForm):
        resp = self.ReqAndRespone(CMD_SM_REGISTER, registerForm, self.REQ_WEB_PATH)
        print resp


if __name__ == '__main__':
    sm = SMServicCli()
    sm.register(RegisterForm("15111111", "15652750943", "password"))
