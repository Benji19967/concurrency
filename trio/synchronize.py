"""
Trio provies open_memory_channel() to communicate, which
acts similar to queue.Queue()
"""

import time
from typing import List
from unittest import result
import trio
from pydantic import BaseModel

class Message(BaseModel):
    index: int


async def long_task(task_id: int, results: List[str]):
    print(f"Starting long task {task_id}")
    await trio.sleep(task_id)
    print(f"Done long task {task_id}")
    result = f"Long task result {task_id}"
    results.append(result)
    return result

async def main():
    print("Starting main")
    start = time.time()

    results = []
    async with trio.open_nursery() as nursery:
        for i in range(5):
            nursery.start_soon(long_task, i, results)
    print(time.time() - start)
    print(results)

trio.run(main)