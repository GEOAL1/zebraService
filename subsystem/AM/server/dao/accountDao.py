# /usr/bin/python
# coding: utf-8
from framework.dao.iMysqlDao import IMysqlDao
from framework.utils.mysqldb import MysqlMananger


class AccountDao(IMysqlDao):
    def __init__(self):
        self.db = MysqlMananger.createMysqlDBInstance("testam")
    pass


    def getAccountInfoByID(self,accountID):
        #根据数据库，选择是否存在
        sql = "select * from t_account where accid=%s"
        return self.db.get(sql,accountID)

    def add(self):
        #插入新纪录，并返回用户id
        sql = "insert into t_account values()"
        return self.db.execute(sql)



if __name__ == '__main__':
    ud = AccountDao()
    result = ud.add()
    print type(result)
    print(result)
    
    ret = ud.getAccountInfoByID("100000018")
    print(ret)
    
    pass
