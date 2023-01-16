#!/usr/bin/env python3
"""inserts new document"""


def insert_school(mongo_collection, **kwargs):
    """function which inserts new document into a collection
    based on kwargs"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
