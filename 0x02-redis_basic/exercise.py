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
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key


    def get(self, key:str, fn: Optional[Callable] = None) -> Union[str, int, float, bytes]:
        """
        takes a key: argument and an optional 
        calable argument called fn: fn will be used to 
        convert data back to the desired type
        """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data
       
    def get_str(self, data:str) -> str:
        """
        this method will automatically parametirize catche.get
        to the correct conversion function
        """
        return data.decode('utf-8')  
    def get_int(self, data: int) -> int:
        """
        that will automatically parametrize Cache.get with the correct conversion function.
        """
        return int(data)