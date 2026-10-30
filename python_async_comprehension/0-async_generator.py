#!/usr/bin/env python3
"""Defines an asynchronous generator that yields random numbers"""

import asyncio
import random


async def async_generator() -> float:
    """Yield 10 random numbers asynchronously, waiting one second each time"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)