#!/usr/bin/env python3
"""
lista all documents in a mongo collection
"""

from typing import List


def list_all(mongo_collection) -> List:

    """returns an empty list if no document is in collection"""
    if mongo_collection is not None:
        return mongo_collection.find()
    return []
