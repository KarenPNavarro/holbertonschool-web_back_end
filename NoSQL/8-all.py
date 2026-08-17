#!/usr/bin/env python3
"""List all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """Return a list of all documents in a collection.

    Args:
        mongo_collection: The pymongo collection object to query.

    Returns:
        A list of all documents in the collection, or an empty list
        if the collection has no document.
    """
    return list(mongo_collection.find())
