from abc import abstractmethod

from framework.utils.mysqldb import MysqlMananger


class IMysqlDao():
    db = MysqlMananger.createMysqlDBInstance()

    @abstractmethod
    def add(self, object):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def selectAll(self):
        pass
