#!/usr/bin/env python3
"""top_students"""


def top_students(mongo_collection):
    """function that returns all students sorted by
    average score"""
    doc = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return doc
