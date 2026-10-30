#!/usr/bin/env python3
"""Module that contains an asynchronous comprehension"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers from an asynchronous generator"""
    return [number async for number in async_generator()]