from abc import abstractmethod

from framework.utils.mysqldb import MysqlMananger


class IMysqlDao():

    def __init__(self):
        pass


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
