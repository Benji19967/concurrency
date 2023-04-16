import trio


async def double_sleep(x):
    print("HEY!")
    await trio.sleep(2 * x)
    print("HO")
    await trio.sleep(2 * x)
    print("DONE")


if __name__ == "__main__":
    trio.run(double_sleep, 1)
