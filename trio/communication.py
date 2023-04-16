"""
Trio provies open_memory_channel() to communicate, which
acts similar to queue.Queue()
"""

import time
import trio
from pydantic import BaseModel


class Message(BaseModel):
    index: int


async def dummy():
    print("Dummy")


async def long_task(task_id: int):
    print(f"Starting long task {task_id}")
    await trio.sleep(1)
    print(f"Done long task {task_id}")
    return f"Long task result {task_id}"


async def main():
    print("Starting main")
    start = time.time()
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)

        print("Before sleep 1")
        time.sleep(2)
        print("After sleep 1")
        nursery.start_soon(dummy)

        print("Before sleep 2")
        time.sleep(2)
        print("After sleep 2")

        # Nursery functions get start here

    print(time.time() - start)


async def producer(send_channel):
    print("Starting producer")
    async with send_channel:
        for i in range(3):
            message = Message(index=i)
            print("Producer: ", id(message))
            await send_channel.send(message)


async def consumer(receive_channel):
    print("Starting consumer")
    messages = []
    async with receive_channel:
        async for message in receive_channel:
            print("Consumer: ", id(message))
            print(f"Message index: {message.index}")
            await long_task(task_id=message.index)
            messages.append(message)
    print("Returning messages")
    return messages


trio.run(main)
