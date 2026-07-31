#!/usr/bin/env python3
"""Module containing a function that sums integers and floats."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list containing integers and floats."""
    return float(sum(mxd_lst))
