#!/usr/bin/env python3
"""
updates a mongodb collection
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """updates a mongo ducument"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
