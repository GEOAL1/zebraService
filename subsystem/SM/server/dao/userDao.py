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

    def getUserByPhoneAndPassword(self, phone, password):
        sql = "select * from t_user where phone = %s and password = %s"
        return self.db.get(sql, phone, password)

    def getUserAllInfoByUserID(self, uid):
        sql = "select * from t_user a join t_user_info b on a.uid = %s and b.uid = %s join t_user_state c" \
              " on a.uid = %s and c.uid = %s;"
        return self.db.get(sql, uid, uid, uid, uid)

if __name__ == '__main__':
    ud = UserDao()
    result = ud.getUserAllInfoByUserID("1433822443")
    print type(result)
    pass
