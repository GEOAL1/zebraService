# /usr/bin/python
# coding: utf-8
# Createtime 2015/5/25 by eric
import torndb


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MysqlMananger(Singleton):
    db = torndb.Connection("127.0.0.1", "zebra", "root", "123456")
