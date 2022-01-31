#!/usr/bin/env python3
from ctypes import Union
from ctypes.wintypes import INT
import redis
import uuid
from typing import Callable, Optional, Union
class Cache:
    def __init__(self):
        """stores an instance of reddis"""
        self._redis = redis.Redis()

        """flush the instance"""
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes data argument and returns a string"""
        key: uuid.UUID = str(uuid.uuid4())
        self._redis.set(key, data)
        return key



    def get(self, key:str, fn: Optional[Callable]=None) -> Union[str, int, float, bytes]:
        """
        takes a key: argument and an optional 
        calable argument called fn: fn will be used to 
        convert data back to the desired type
        """
        valk = self._redis.get(key)
        if valk is not None:
            val_conv = fn(valk)
            return val_conv
        return valk

    def get_str(self, key: str) -> str:
        """
        this method will automatically parametirize catche.get
        to the correct conversion function
        """
        data = self._redis.get(key, lambda x: x.decode('utf-8'))
        return data

    def get_int(self, key: int) -> int:
        """
        that will automatically parametrize Cache.get with the correct conversion function.
        """
        data = self._redis.get(key, lambda x: int(x))
        return data
        