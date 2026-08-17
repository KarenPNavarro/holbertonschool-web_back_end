#!/usr/bin/env python3
"""Find schools by topic in a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object to query.
        topic: The topic to search for.

    Returns:
        A list of school documents that have the given topic.
    """
    return list(mongo_collection.find({"topics": topic}))
