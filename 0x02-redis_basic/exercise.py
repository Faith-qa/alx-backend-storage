#!/usr/bin/env python3
"""
writting string to redis
"""

import redis
from uuid import uuid4
from typing import Callable, Union, ValuesView
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    a decorator that takes a single method and returns a callable
    """
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped function that increment key"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper

class Cache:
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes data args and returns a string
        generates a random key and stores input
        in redis
        """
        key = str(uuid4())
        self._redis.set(key, data)

        return key
    
    def get(self,  key: str, fn: Callable = None):
        """converts redis data back to desired format"""
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Parametize Cache.get to str"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """parametizes Cache.get to int"""
        data = self._redis.get(key)
        return data.decode("utf-8")
