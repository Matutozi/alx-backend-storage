#!/usr/bin/env python3
"""
SCRIPT THAT UPDATES A DOCUMENT IN A COLLECTION
"""


def update_topics(mongo_collection, name, topics):
    """
    method: function that updates document in a collection
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
