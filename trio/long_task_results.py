"""
Getting results from a long async task

Examples from the web:

- https://github.com/megadose/holehe/blob/0f53de6e98419dbea24c187a93c897ad7fbbb68c/holehe/core.py#L213
- https://github.com/srush/MiniChain/blob/a29fbb3bc0311f6c4c98ffd19d26f4d6a5e1e76d/minichain/base.py#L165
"""

import time
from typing import List
import trio

async def long_task(task_id: int, results: List[str]):

    print(f"Starting long task {task_id}")
    await trio.sleep(2)
    print(f"Done long task {task_id}")
    result = f"Long task result {task_id}"
    results.append(result)
    return result


async def main():
    """
    Order of results is not guaranteed to be the same for every run
    """
    print("Starting main")
    start = time.time()

    results = []
    async with trio.open_nursery() as nursery:
        for i in range(5):
            nursery.start_soon(long_task, i, results)
    print(time.time() - start)
    print(results)


trio.run(main)
