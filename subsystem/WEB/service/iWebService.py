# /usr/bin/python
# coding: utf-8
import logging
from subsystem.AM.amService import AMService
from subsystem.CM.cmService import CMService
from subsystem.DM.dmService import DMService
from subsystem.SM.smService import SMService

log = logging.getLogger("iWebService")


class IWebService:
    def __init__(self, sm=SMService(), cm=CMService(), am=AMService(), dm=DMService()):
        self.sm = sm;
        self.cm = cm;
        self.am = am;
        self.dm = dm;
        pass
