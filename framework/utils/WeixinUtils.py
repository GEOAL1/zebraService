# /usr/bin/python
# coding: utf-8
import time

import redis
from wechat_sdk import WechatBasic


class WeixinMananger:
    def __init__(self, appid="wxc2b14fc7557dc863", appsecret="67c0097d1bf2f7804f9eb2375f3d2039",
                 redisIp="127.0.0.1", redisPort=6379):
        self.redis = redis.StrictRedis(host=redisIp)
        self.appid = appid;
        self.appsecret = appsecret;
        self.wechat = WechatBasic(appid=appid, appsecret=appsecret);

    def __getRedisWXAccessToken(self):
        return self.redis.get("wx_access_token")

    def __getRedisWXJsApiToken(self):
        return self.redis.get("wx_jsapi_token")

    def getAccessToken(self):
        token = self.__getRedisWXAccessToken()
        if token is None:
            token = self.wechat.grant_token()
            if token != None:
                timeout = token["expires_in"]
                self.redis.setex("wx_access_token", timeout, token["access_token"])
                return token["access_token"]
            else:
                return None;
        else:
            return token

    def getJsApiToken(self):
        ticket = self.__getRedisWXJsApiToken()
        if ticket is None:
            print self.getAccessToken()
            ticket = self.wechat.grant_jsapi_ticket()
            if (ticket != None):
                timeout = ticket["expires_in"];
                self.redis.setex("wx_jsapi_token", timeout, ticket["ticket"])
                return ticket["ticket"]
            else:
                return None
        else:
            return ticket

    def getJsJDK(self, srcUrl):
        timestamp = int(time.time())
        noncestr = str(time.time())
        url = srcUrl
        jsApiToken = self.getJsApiToken();
        data = {};
        data["timestamp"] = timestamp
        data["nonceStr"] = noncestr
        data["appId"] = self.appid
        data["signature"] = self.wechat.generate_jsapi_signature(timestamp, noncestr, url, jsApiToken)
        data["jsApiList"] = ["openLocation", "getLocation", "scanQRCode", "showMenuItems"]
        data["debug"] = True
        return data


if __name__ == '__main__':
    wxm = WeixinMananger();
    print wxm.getJsApiToken()
    print wxm.getJsJDK("http://www.baidu.com")
    # print uuid._random_getnode()
