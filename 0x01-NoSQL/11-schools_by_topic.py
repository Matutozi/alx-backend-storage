#!/usr/bin/env python3
"""
script that finds document in a collection"
"""


def schools_by_topic(mongo_collection, topic):
    """
    method : finds the collection
    """
    return mongo_collection.find({"topics": topic})
