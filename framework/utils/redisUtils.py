import redis


class RedisDBConfig:
    HOST = '127.0.0.1'
    PORT = 6379
    DBID = 0


def operator_status(func):
    '''''get operatoration status 
    '''

    def gen_status(*args, **kwargs):
        error, result = None, None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            error = str(e)
            print(error)

        return result

    #         return {'result': result, 'error':  error}

    return gen_status


class RedisCache(object):
    def __init__(self):
        if not hasattr(RedisCache, 'pool'):
            RedisCache.create_pool()
        self._connection = redis.Redis(connection_pool=RedisCache.pool)

    @staticmethod
    def create_pool(host=RedisDBConfig.HOST,port = RedisDBConfig.PORT,db=RedisDBConfig.DBID):
        RedisCache.pool = redis.ConnectionPool(
            host=host,
            port=port,
            db=db)

    @operator_status
    def set_data(self, key, value):
        '''''set data with (key, value) 
        '''
        return self._connection.set(key, value)

    @operator_status
    def get_data(self, key):
        '''''get data by key 
        '''
        return self._connection.get(key)

    @operator_status
    def del_data(self, key):
        '''''delete cache by key 
        '''
        return self._connection.delete(key)

    @operator_status
    def hset_data(self, name, key, value):
        return self._connection.hset(name, key, value)

    @operator_status
    def hmset_data(self, name, mapping):
        return self._connection.hmset(name, mapping)

    @operator_status
    def hget_data(self, name, key):
        return self._connection.hget(name, key)

    @operator_status
    def hmget_data(self, name, keys):
        return self._connection.hmget(name, keys)

    @operator_status
    def hdel_data(self, name):
        return self._connection.hdel(name)

    def getInstance(self):
        return self._connection

    @operator_status
    def listBlpop(self, name):
        return self._connection.blpop(name, 0)

    @operator_status
    def listRpush(self, name, value):
        return self._connection.rpush(name, value)


if __name__ == '__main__':
    #     print RedisCache().set_data('Testkey', "Simple Test")
    #     print RedisCache().get_data('Testkey')
    #     print RedisCache().del_data('Testkey')
    #     print RedisCache().get_data('Testkey')
    RedisCache().listRpush("keys", "xxxxxxxxxxxxxxxxxxxxxxxxxx")
    while (1):
        b = RedisCache().listBlpop("keys")
        print(b)
