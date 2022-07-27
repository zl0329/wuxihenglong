import redis


class RedisConf:
    REDIS_HOST = 'test.geointech.cn'
    REDIS_PORT = 16379
    REDIS_PASS = "Geoin_123456"
    redis_conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS, decode_responses=True)

    def getCode(uuid):
        print('redisopts 连接成功')
        code = RedisConf.redis_conn.get(uuid)
        # RedisConf.redis_conn.close()
        return code
        RedisConf.redis_conn.close()
