from aiogram import Router
from aiogram.types import Message, BufferedInputFile
from aiogram.filters import Command

from ..services.csv_creator import create_csv, extract_all_links, extract_links

router = Router()

@router.message(Command('full_csv'))
async def get_full_csv_handler(message: Message):
    user_id: str = str(message.from_user.id)
    links = await extract_all_links(user_id)
    csv_bytes = await create_csv(links)

    await message.answer_document(
        document=BufferedInputFile(
            file=csv_bytes,
            filename='links.csv'
        )
    )


@router.message(Command('csv'))
async def get_csv_handler(message: Message):
    user_id: str = str(message.from_user.id)
    links = await extract_links(user_id)
    csv_bytes = await create_csv(links)

    await message.answer_document(
        document=BufferedInputFile(
            file=csv_bytes,
            filename='links.csv'
        )
    )


@router.message(Command('all_links'))
async def get_links(message: Message):
    user_id: str = str(message.from_user.id)
    links = await extract_links(user_id)
    text = '\n'.join(', '.join(str(field) for field in link) for link in links)
    await message.answer(text=text)