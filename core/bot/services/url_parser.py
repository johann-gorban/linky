import sys
from aiogram.types import MessageEntity
from typing import List

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from database.crud import db

async def extract_url(text: str, entities: List[MessageEntity]) -> List[str]:
    urls = []
    if entities is None:
        return urls
    
    for entity in entities:
        if entity.type == 'url':
            url = text[entity.offset : entity.offset + entity.length]
            urls.append(url)
        elif entity.type == 'text_link' and entity.url is not None:
            urls.append(entity.url)

    return urls


async def record_link(url: str, message_id: str, user_id: str, chat_id: str):
    await db.add_link(
        url=url,
        message_id=message_id,
        user_id=user_id,
        chat_id=chat_id
    )