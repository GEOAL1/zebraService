#/usr/bin/python
#coding: utf-8
import logging
from subsystem.SM.smService import SMService

log = logging.getLogger("userService")

class UserServer():
    def __init__(self,sm=SMService(),cm=SMService(),am=SMService(),dm=SMService()):

        pass