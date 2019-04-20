import redis

class cacheMonkey:
    def __init__(self, host, port, password):
        self.redis_host = host
        self.redis_port = port
        self.redis_password = password
        self.conn = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)

    def latency_monitor(self, keys):
        '''Sends requests to keys at the rate of 60 per minute and records the latency'''


    def delete_cache(self):
        '''Clears the cache'''
        self.conn.flushall(asynchronous=False)

    def set_replacement_policy(self, policy):
        '''Sets the replacement policy as LRU or Random on the proxy server'''


    def set_ttl(self, ttl):
        '''Sets the TTL of cached entries'''
