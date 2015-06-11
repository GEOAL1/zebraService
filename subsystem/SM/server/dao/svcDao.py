# /usr/bin/python
# coding: utf-8
from _mysql_exceptions import IntegrityError
from framework.dao.iMysqlDao import IMysqlDao
from framework.model import Svc
from framework.utils.mysqldb import MysqlMananger


class SvcDao(IMysqlDao):
    def __init__(self):
        self.db = MysqlMananger.createMysqlDBInstance("db_zebra_sm", "127.0.0.1", "root", "123456")

    pass

    def createService(self, uid, did):
        sid = self.db.execute("insert into t_service(did,uid)  VALUES (did,uid)")
        return Svc(uid=uid, did=did, sid=sid)
        pass


if __name__ == '__main__':
    sd = SvcDao();
    rs = sd.createService(111, 222)
