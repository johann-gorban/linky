from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(lambda message: not message.text.startswith('/'))
async def echo_new_message(message: Message):
    chat_id = message.chat.id if message.chat else None
    user_id = message.from_user.id if message.from_user else None
    msg_id = message.message_id
    text = message.text

    print(f"[NEW MESSAGE] chat_id={chat_id}, user_id={user_id}, msg_id={msg_id}, text={text}")
