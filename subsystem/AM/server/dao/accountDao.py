# /usr/bin/python
# coding: utf-8
from framework.dao.iMysqlDao import IMysqlDao
from framework.utils.mysqldb import MysqlMananger


class AccountDao(IMysqlDao):
    def __init__(self):
        self.db = MysqlMananger.createMysqlDBInstance("db_zebra_am")
    pass


    def getAccountInfoByID(self,accountID):
        #根据数据库，选择是否存在
        sql = "select * from t_user where accountID=%s"
        return self.db.get(sql,accountID)

    def add(self):
        #插入新纪录，并返回用户id
        return None



if __name__ == '__main__':
    ud = AccountDao()
    result = ud.getUserAllInfoByUserID("1433822443")
    print type(result)
    pass
