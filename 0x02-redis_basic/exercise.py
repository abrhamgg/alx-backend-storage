#!/usr/bin/env python3
"""
 a Cache class
 generate a random key (e.g. using uuid),
 store the input data in Redis using the random key and return the key.
"""

from typing import Callable, Optional, Union
from functools import wraps
import redis
import sys
from uuid import uuid4


class Cache:
    "store an instance of redis client as private variable"

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data in Redis using the random key and return the key
        """
        key: str = str(uuid4())
        value = data
        self._redis.set(key, value)
        return key

    def get_str(self, key: str) -> str:
        """ converts byte to str """
        data = self._redis.get(key)
        return data.decode('UTF-8')

    def get_int(self, key: str) -> int:
        data = self._redis.get(key)
        try:
            data = int(data.decode('UTF-8'))
        except Exception:
            data = 0
        return data

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Gets  """
        res = self._redis.get(key)
        try:
            res = fn(res) if fn else res
        except ValueError as err:
            pass
        return
