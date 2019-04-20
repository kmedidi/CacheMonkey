import cacheMonkey

def delete_test(CM):
    '''Trigger deletion testing'''
    CM.delete_cache()
    CM.latency_monitor()

def replace_test(CM):
    '''Trigger replacement policy testing'''
    CM.set_replacement_policy('LRU')
    CM.latency_monitor()
    CM.set_replacement_policy('RR')
    CM.latency_monitor()

def stale_test(CM):
    '''Trigger stale time testing'''
    CM.set_ttl(100)
    CM.latency_monitor()
    CM.set_ttl(200)
    CM.latency_monitor()

CM = cacheMonkey()
delete_test(CM)
replace_test(CM)
stale_test(CM)
