from aiogram import Router, F
from aiogram.types import Message

from ..services.url_parser import record_link, extract_url

router = Router()

@router.message(lambda message: not message.text.startswith('/'))
async def parse_message(message: Message):
    chat_id = message.chat.id if message.chat else None
    user_id = message.from_user.id if message.from_user else None
    msg_id = message.message_id
    text = message.text

    urls = await extract_url(text, message.entities)

    for url in urls:
        await record_link(
            url=url,
            message_id=msg_id,
            user_id=user_id,
            chat_id=chat_id
        )