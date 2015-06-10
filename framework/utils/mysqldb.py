# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25 by eric
import torndb





class MysqlMananger:

    def __init__(self):
        pass

    @staticmethod
    def createMysqlDBInstance(dbname="testam",host="10.111.32.95",username="root",password="root"):
        return torndb.Connection(host, dbname, username, password)
