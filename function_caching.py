# A technique for improving performance of functions by caching their results.
# This is especially useful for functions that are computationally expensive and are called multiple times with the same arguments.
from functools import lru_cache
import time
# This decorator caches the results of the
# function it decorates. The maxsize parameter specifies the maximum number of results to cache. If set to None, the cache can grow indefinitely.
def fx(n):
    time.sleep(5)
    return n * 5
print(fx(10)) # This will take 5 seconds to compute and cache the result.
print("Second call:")
def fx(n):
    time.sleep(5)
    return n * 5
print(fx(10)) # This will take 5 seconds to compute and cache the result.
print("Second call:")