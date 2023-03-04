"""
Trio provies open_memory_channel() to communicate, which
acts similar to queue.Queue()
"""

import time
import trio
from pydantic import BaseModel

class Message(BaseModel):
    index: int


async def main():
    start = time.time()
    async with trio.open_nursery() as nursery:
        send_channel, receive_channel = trio.open_memory_channel(0)
        nursery.start_soon(producer, send_channel)
        nursery.start_soon(consumer, receive_channel)
    print(time.time() - start)


async def producer(send_channel):
    async with send_channel:
        for i in range(100000):
            message = Message(index=i)
            print("Producer: ", id(message))
            await send_channel.send(message)


async def consumer(receive_channel):
    async with receive_channel:
        async for message in receive_channel:
            print("Consumer: ", id(message))
            print(f"Message index: {message.index}")


trio.run(main)