#!/usr/bin/env python3
"""
SCRIPT THAT INSERTS A NEW DOCUMENT INTO A COLLECTION
"""


def insert_school(mongo_collection, **kwargs):
    """
    method: inserts a new document in a collection
    """
    return mongo_collection.insert_one(kwargs).inserted_id
