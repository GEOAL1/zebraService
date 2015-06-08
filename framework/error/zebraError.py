# /usr/bin/python
# coding: utf-8


class ZebraError(StandardError):
    def __init__(self, erroCode, errorMsg):
        self.errCode = erroCode;
        self.errMsg = errorMsg;

    def setErrorCode(self, code):
        self.errCode = code;
        return self

    def setErrorMessage(self, message):
        self.errMsg = message;

    pass


class InputArgsError(ZebraError):
    def __init__(self):
        self.errCode = -1000
        self.errMsg = "输入的参数有误"
        pass

    pass


class UnameOrPasswordError(ZebraError):
    def __init__(self):
        self.errCode = -1001
        self.errMsg = "用户名或密码不正确"
        pass

    pass


class CreateUserError(ZebraError):
    def __init__(self):
        self.errCode = -1002
        self.errMsg = "注册用户失败"
        pass

    pass


class ValidateCodeError(ZebraError):
    def __init__(self):
        self.errCode = -1003
        self.errMsg = "错误的验证码"
        pass

    pass


class SamePasswordError(ZebraError):
    def __init__(self):
        self.errCode = -1004
        self.errMsg = "两次输入的密码不相同"
        pass

    pass


class ExistedPhoneError(ZebraError):
    def __init__(self):
        self.errCode = -1005
        self.errMsg = "已经存在的手机号"
        pass

    pass


class RegInerError(ZebraError):
    def __init__(self):
        self.errCode = -1006
        self.errMsg = "注册失败，内部错误"
        pass

    pass


class SendMessageApiError(ZebraError):
    def __init__(self):
        self.errCode = -1007
        self.errMsg = "调用发送API失败"
        pass

    pass


class UserIsNotFoundedError(ZebraError):
    def __init__(self):
        self.errCode = -1008
        self.errMsg = "没有找到该用户"
        pass

    pass


class GenOrderError(ZebraError):
    def __init__(self):
        self.errCode = -1009
        self.errMsg = "生成订单失败"
        pass


pass


class OrderNotFoundError(ZebraError):
    def __init__(self):
        self.errCode = -1010
        self.errMsg = "没有找到该订单"
        pass


pass


class OrderOwnerError(ZebraError):
    def __init__(self):
        self.errCode = -1011
        self.errMsg = "订单的用户不匹配"
        pass


pass


class FinishOrderError(ZebraError):
    def __init__(self):
        self.errCode = -1012
        self.errMsg = "取消订单失败"
        pass


pass


class BikeNotFoundError(ZebraError):
    def __init__(self):
        self.errCode = -1013
        self.errMsg = "没有该车的信息"
        pass


pass


class UserOrderNotFoundError(ZebraError):
    def __init__(self):
        self.errCode = -1014
        self.errMsg = "没有找到该用户的ID"
        pass


pass


class InvaildReqCodeError(ZebraError):
    def __init__(self):
        self.errCode = -1014
        self.errMsg = "无效的请求类型"
        pass


pass
