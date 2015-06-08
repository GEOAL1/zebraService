# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25 by eric
import torndb





class MysqlMananger:

    def __init__(self):
        pass

    @staticmethod
    def createMysqlDBInstance(dbname="zebra",host="127.0.0.1",username="root",password="123456"):
        return torndb.Connection(host, dbname, username, password)
