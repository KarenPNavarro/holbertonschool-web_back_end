#!/usr/bin/env python3
"""
Concurrent coroutines
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Execute wait_random n times concurrently.
    """

    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    delays = []

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
