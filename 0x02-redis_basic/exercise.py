#!/usr/bin/env python3
from ctypes import Union
from ctypes.wintypes import INT
import redis
import uuid
from typing import Callable, Optional, Union
class Cache:
    def __init__(self):
        """construct the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store new data and return a new uuid"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get the element and return the decoded version"""
        data = self._redis.get(key)
        if (fn is not None):
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """ return the decoded byte in string """
        return data.decode('utf-8')

    def get_int(self, data: str) -> int:
        """ return the decoded byte in integer """
        return int(data)
    