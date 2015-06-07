# /usr/bin/python
# coding: utf-8
from json.encoder import JSONEncoder
from json.decoder import JSONDecoder


class JsonBikeDy():
    def __init__(self):
        pass

    __bike_id = None
    __cur_power = None
    __throttle_state = None
    __brake_state = None
    __motor_state = None
    __lock_state = None
    __indicator_state = None
    __longitude = None
    __latitude = None
    __speed = None
    __requestCode = None
    __timeSamp = None
    __uuid = None

    def setBikeID(self, bikeid):
        self.__bike_id = bikeid

    def getBikeID(self):
        return self.__bike_id

    def setCurPower(self, cur_power):
        self.__cur_power = cur_power

    def getCurPower(self):
        return self.__cur_power

    def setThrottleState(self, throttle_state):
        self.__throttle_state = throttle_state

    def getThrottleState(self):
        return self.__throttle_state

    def setBrakeState(self, brake_state):
        self.__brake_state = brake_state

    def getBrakeState(self):
        return self.__brake_state

    def setMotorState(self, motor_state):
        self.__motor_state = motor_state

    def getMotorState(self):
        return self.__motor_state

    def setLockState(self, lock_state):
        self.__lock_state = lock_state

    def getLockState(self):
        return self.__lock_state

    def setIndicatorState(self, indicator_state):
        self.__indicator_state = indicator_state

    def getIndicatorState(self):
        return self.__indicator_state

    def setLongitude(self, longitude):
        self.__longitude = longitude

    def getLongitude(self):
        return self.__longitude

    def setLatitude(self, latitude):
        self.__latitude = latitude

    def getLatitude(self):
        return self.__latitude

    def setSpeed(self, speed):
        self.__speed = speed

    def getSpeed(self):
        return self.__speed

    def setRequestCode(self, requestCode):
        self.__requestCode = requestCode

    def getRequestCode(self):
        return self.__requestCode

    def setTimeSamp(self, timeSamp):
        self.__timeSamp = timeSamp

    def getTimeSamp(self):
        return self.__timeSamp

    def setUUID(self, uuid):
        self.__uuid = uuid

    def getUUID(self):
        return self.__uuid

    def tojsonStr(self):
        body = {}
        body['bike_id'] = self.__bike_id
        body['cur_power'] = self.__cur_power
        body['throttle_state'] = self.__throttle_state
        body['brake_state'] = self.__brake_state
        body['motor_state'] = self.__motor_state
        body['lock_state'] = self.__lock_state
        body['indicator_state'] = self.__indicator_state
        body['longitude'] = self.__longitude
        body['latitude'] = self.__latitude
        body['speed'] = self.__speed
        head = {}
        head['requestCode'] = self.__requestCode
        head['timeSamp'] = self.__timeSamp
        head['uuid'] = self.__uuid
        jsonStr = {}
        jsonStr['body'] = body
        jsonStr['head'] = head
        return JSONEncoder().encode(jsonStr)

    def decodeJson(self, strJson):
        json = JSONDecoder().decode(strJson)
        body = json["body"]
        head = json["head"]
        if body is None:
            return None
        if head is None:
            return None
        if body['bike_id'] is not None:
            self.__bike_id = body['bike_id']
        if body['cur_power'] is not None:
            self.__cur_power = body['cur_power']
        if body['throttle_state'] is not None:
            self.__throttle_state = body['throttle_state']
        if body['brake_state'] is not None:
            self.__brake_state = body['brake_state']
        if body['brake_state'] is not None:
            self.__brake_state = body['brake_state']
        if body['motor_state'] is not None:
            self.__motor_state = body['motor_state']
        if body['lock_state'] is not None:
            self.__lock_state = body['lock_state']
        if body['indicator_state'] is not None:
            self.__indicator_state = body['indicator_state']
        if body['longitude'] is not None:
            self.__longitude = body['longitude']
        if body['latitude'] is not None:
            self.__latitude = body['latitude']
        if body['speed'] is not None:
            self.__speed = body['speed']
        if head['requestCode'] is not None:
            self.__requestCode = head['requestCode']
        if head['timeSamp'] is not None:
            self.__timeSamp = head['timeSamp']
        if head['uuid'] is not None:
            self.__uuid = head['uuid']
        return "OK"


class JsonBikeCtl():
    def __init__(self):
        pass

    __bike_id = None
    __power = None
    __lockBike = None
    __indicatorLight = None
    __horn = None
    __requestCode = None
    __timeSamp = None
    __uuid = None

    def setBikeID(self, bikeid):
        self.__bike_id = bikeid

    def getBikeID(self):
        return self.__bike_id

    def setPower(self, power):
        self.__power = power

    def getPower(self):
        return self.__power

    def setLockBike(self, lockBike):
        self.__lockBike = lockBike

    def getLockBike(self):
        return self.__lockBike

    def setIndicatorLight(self, indicatorLight):
        self.__indicatorLight = indicatorLight

    def getIndicatorLight(self):
        return self.__indicatorLight

    def setHorn(self, horn):
        self.__horn = horn

    def getHorn(self):
        return self.__horn

    def setRequestCode(self, requestCode):
        self.__requestCode = requestCode

    def getRequestCode(self):
        return self.__requestCode

    def setTimeSamp(self, timeSamp):
        self.__timeSamp = timeSamp

    def getTimeSamp(self):
        return self.__timeSamp

    def setUUID(self, uuid):
        self.__uuid = uuid

    def getUUID(self):
        return self.__uuid

    def tojsonStr(self):
        body = {}
        body['bike_id'] = self.__bike_id
        body['power'] = self.__power
        body['lockBike'] = self.__lockBike
        body['indicatorLight'] = self.__indicatorLight
        body['horn'] = self.__horn
        head = {}
        head['requestCode'] = self.__requestCode
        head['timeSamp'] = self.__timeSamp
        head['uuid'] = self.__uuid
        jsonStr = {}
        jsonStr['body'] = body
        jsonStr['head'] = head
        return JSONEncoder().encode(jsonStr)

    def decodeJson(self, strJson):
        json = JSONDecoder().decode(strJson)
        body = json["body"]
        head = json["head"]
        if body is None:
            return None
        if head is None:
            return None
        if body['bike_id'] is not None:
            self.__bike_id = body['bike_id']
        if body['power'] is not None:
            self.__power = body['power']
        if body['lockBike'] is not None:
            self.__lockBike = body['lockBike']
        if body['indicatorLight'] is not None:
            self.__indicatorLight = body['indicatorLight']
        if body['horn'] is not None:
            self.__horn = body['horn']
        if head['requestCode'] is not None:
            self.__requestCode = head['requestCode']
        if head['timeSamp'] is not None:
            self.__timeSamp = head['timeSamp']
        if head['uuid'] is not None:
            self.__uuid = head['uuid']
        return "OK"


if __name__ == '__main__':
    b = JsonBikeCtl()
    b.setBikeID("111")
    b.setHorn("1")
    b.setIndicatorLight("0")
    b.setLockBike("1")
    b.setPower("0")
    b.setRequestCode("1")
    b.setTimeSamp("0")
    b.setUUID("1")
    print(b.tojsonStr())

    b.decodeJson(b.tojsonStr())

    print(b.getBikeID())

    c = JsonBikeDy()
    c.setBikeID("s")
    c.setBrakeState("1")
    c.setRequestCode("1")
    c.setTimeSamp("0")
    c.setUUID("1")
    print(c.tojsonStr())

    c.decodeJson(c.tojsonStr())

    print(c.getBikeID())
