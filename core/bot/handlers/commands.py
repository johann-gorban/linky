from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from database.crud import db

router = Router()

@router.message(Command("all_links"))
async def all_links_handler(message: Message):
    if message.chat.type == "private":
        links = await db.get_all_links()
        text = "\n".join([link.url for link in links]) or "No links found"
        await message.answer(text)
    else:
        links = await db.get_links_by_chat_id(str(message.chat.id))
        text = "\n".join([link.url for link in links]) or "No links found for that chat"
        await message.answer(text)


@router.message(Command("user_links"))
async def user_links_handler(message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Enter user_id: /user_links <id>")
        return
    user_id = args[1]
    links = await db.get_links_by_user_id(user_id)
    text = "\n".join([link.url for link in links]) or "No links found for that user"
    await message.answer(text)


@router.message(Command("chat_links"))
async def chat_links_handler(message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Enter chat_id: /chat_links <id>")
        return
    chat_id = args[1]
    links = await db.get_links_by_chat_id(chat_id)
    text = "\n".join([link.url for link in links]) or "No links found for that chat"
    await message.answer(text)
