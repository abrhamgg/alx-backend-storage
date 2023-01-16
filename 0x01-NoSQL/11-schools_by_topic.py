#!/usr/bin/env python3
"""search collection"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    result = mongo_collection.find({"topic": topic})
    return result
