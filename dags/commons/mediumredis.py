from redis import ConnectionPool, Redis
#redis_host = BaseHook.get_connection('redis').host

class MediumRedis:
    redis_con: Redis
    
    def __init__(self):
        pool = ConnectionPool(host="localhost",
                            db=0,
                            port= 6379)
        self.redis_con = Redis(connection_pool=pool)
        

    def get(self, key):
        return self.redis_con.get(key)
    
    def set(self, key, value):
        return self.redis_con.set(key, value)
    
    def lrange(self, key):
        return self.redis_con.lrange(key, 1, 100)
    