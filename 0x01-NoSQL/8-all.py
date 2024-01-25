#!/usr/bin/env python3
"""
mod doc
"""


def list_all(mongo_collection):
    """
    method: list all document in collection
    """
    return list(mongo_collection.find())
