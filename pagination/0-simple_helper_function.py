#!/usr/bin/env python3
"""Simple pagination helper module.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for a given pagination.

    Args:
        page: The 1-indexed page number.
        page_size: The number of items per page.

    Returns:
        A tuple (start_index, end_index) corresponding to the range of
        indexes to return in a list for those pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
