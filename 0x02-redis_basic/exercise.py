#!/usr/bin/env python3
"""
writting string to redis
"""

import redis
from uuid import uuid4
from typing import Callable, Union, ValuesView
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    a decorator to store the history of inputs of a particular
    function
    """
    method_key = method.__qualname__
    input_key = method_key + ":inputs"
    output_key = method_key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """stores data in redis db"""
        self._redis.rpush(input_key, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(output_key, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    a decorator that takes a single method and returns a callable
    """
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped function that increment key"""
        self._redis.incr(method_key)
        return method(self, *args, **kwds)
    return wrapper


def replay(method: Callable):
    """ display the history call """
    method_key = method.__qualname__
    inputs = method_key + ":inputs"
    outputs = method_key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(method_key).decode("utf-8")
    print("{} was called {} times:".format(method_key, count))
    ListInput = redis.lrange(inputs, 0, -1)
    ListOutput = redis.lrange(outputs, 0, -1)
    allData = list(zip(ListInput, ListOutput))
    for key, data in allData:
        attr, data = key.decode("utf-8"), data.decode("utf-8")
        print("{}(*{}) -> {}".format(method_key, attr, data))



class Cache:
    def __init__(self):
        """constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
