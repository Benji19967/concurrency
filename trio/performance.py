import httpx
import trio
import time

URL = "http://0.0.0.0:8989/v1/health_check"
NUM_REQUESTS = 5000


async def main():
    start = time.time()
    async with httpx.AsyncClient() as client:
        async with trio.open_nursery() as nursery:
            for _ in range(NUM_REQUESTS):
                print("Sending request")
                nursery.start_soon(client.get, URL)
                print("Sent request")
            print("Sent all requests")
        print("Done")
        print(time.time() - start)


if __name__ == "__main__":
    trio.run(main)
