#!/usr/bin/env python3
"""
writting string to redis
"""

import redis
from uuid import uuid4
from typing import Union


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
