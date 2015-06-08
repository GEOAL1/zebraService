# /usr/bin/python
# coding: utf-8
from framework.dao.iMysqlDao import IMysqlDao
from framework.utils.mysqldb import MysqlMananger


class UserDao(IMysqlDao):
    def __init__(self):
        self.db = MysqlMananger.createMysqlDBInstance("db_zebra_sm")
    pass

    def getUserByPhone(self,phone):
        sql = "select * from t_user where phone=%s"
        return self.db.get(sql,phone)

    def add(self,userid,phone,password):
        sql = "START TRANSACTION;" \
              "insert into t_user(uid, phone, password)  VALUES (%s,%s,%s);" \
              "insert into t_user_info(uid) VALUES(%s);" \
              "insert into t_user_state(uid) VALUES(%s);" \
              "COMMIT;"
        self.db.execute(sql,userid,phone,password,userid,userid)


if __name__ == '__main__':
    ud = UserDao()
    ud.add(123456,15652750944,"123456")
    pass
