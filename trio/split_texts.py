import time
from typing import List
import trio
from core.text import Text


def create_texts(num_texts: int) -> List[Text]:
    return [Text(index=i, input_text=f"P0_{i}|P1_{i}|P2_{i}") for i in range(num_texts)]


async def main():
    print("Starting main")
    start = time.time()
    num_texts = 10

    texts = create_texts(num_texts=num_texts)

    async with trio.open_nursery() as nursery:
        for text in texts:
            nursery.start_soon(text.split_text_into_paragraphs)

    for text in texts:
        print(text.paragraphs)

    print(time.time() - start)


trio.run(main)
