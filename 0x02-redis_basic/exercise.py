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
