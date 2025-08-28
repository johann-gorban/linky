from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command

from ..services.csv_creator import create_csv, extract_all_links, extract_links

router = Router()

@router.message(Command('full_csv'))
async def get_full_csv_handler(message: Message):
    links = await extract_all_links()
    csv_bytes = await create_csv(links)

    await message.answer_document(
        document=BufferedInputFile(
            file=csv_bytes,
            filename='links.csv'
        )
    )


@router.message(Command('csv'))
async def get_csv_handler(message: Message):
    links = await extract_links()
    csv_bytes = await create_csv(links)

    await message.answer_document(
        document=BufferedInputFile(
            file=csv_bytes,
            filename='links.csv'
        )
    )


@router.message(Command('all_links'))
async def get_links(message: Message):
    links = await extract_links()
    text = '\n'.join(', '.join(str(field) for field in link) for link in links)
    await message.answer(text=text)


# @router.message(Command('user_links'))
# async def user_links_handler(message: Message):
#     args = message.text.split()
#     if len(args) < 2:
#         await message.answer('Enter user_id: /user_links <id>')
#         return
#     user_id = args[1]
#     links = await db.get_links_by_user_id(user_id)
#     text = '\n'.join([link.url for link in links]) or 'No links found for that user'
#     await message.answer(text)


# @router.message(Command('chat_links'))
# async def chat_links_handler(message: Message):
#     args = message.text.split()
#     if len(args) < 2:
#         await message.answer('Enter chat_id: /chat_links <id>')
#         return
#     chat_id = args[1]
#     links = await db.get_links_by_chat_id(chat_id)
#     text = '\n'.join([link.url for link in links]) or 'No links found for that chat'
#     await message.answer(text)
