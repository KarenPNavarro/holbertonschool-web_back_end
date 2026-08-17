#!/usr/bin/env python3
"""Update the topics of a school document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """Change all topics of a school document based on its name.

    Args:
        mongo_collection: The pymongo collection object to update.
        name: The name of the school to update.
        topics: The list of topics approached in the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
