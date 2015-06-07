# /usr/bin/python
# coding: utf-8
import urllib

import tornado


class MessageUtile():
    @staticmethod
    def sendValidMessage(phone, code):
        key = "a899cda8e885b07a7b4615011780d2a4"
        template = "3030"
        client = tornado.httpclient.AsyncHTTPClient()
        args = urllib.urlencode(
            {'mobile': phone, 'tpl_id': template, 'tpl_value': "#code#=%s" % (code), 'key': key})

        url = "http://v.juhe.cn/sms/send?%s" % args
        resp = client.fetch(url)
        return resp

    pass
