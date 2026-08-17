#!/usr/bin/env python3
"""Insert a document in a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object to insert into.
        **kwargs: The fields and values of the document to insert.

    Returns:
        The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
