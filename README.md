# CacheMonkey
Chaos Engineering

Cache is component that stores data so that future requests for data can be served faster. The motivation for implement Cache is to improve the following factors.
1. Latency
2. Throughput 

The Caching problem is a classic hard one in Computer Science. The objective of this project is not to re-establish that but to provide test findings that can allow for fine tuning of Caching policy.

Operations
1. Delete cache completely - Measure Latency
2. Checking cache replacement policy (random and LRU) for different loads - Measure Latency
3. Stale cache entries (Feature flags updated) - Measure Latency

Support
REDIS cache 
