from typing import List, Optional
from pydantic import BaseModel
import trio  # type: ignore
import random


async def split_text(text: str) -> List[str]:
    await trio.sleep(random.uniform(0, 1))  # type: ignore
    return text.split("|")


class Text(BaseModel):
    """
    A text can have many paragraphs
    """

    index: int
    input_text: str
    paragraphs: Optional[List[str]] = None

    async def split_text_into_paragraphs(self) -> None:
        self.paragraphs = await split_text(text=self.input_text)
