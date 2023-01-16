#!/usr/bin/env python3
"""list all"""


def list_all(mongo_collection):
    """function which list all document in the collection"""
    result = []
    for doc in mongo_collection.find():
        result.append(doc)
    return result
