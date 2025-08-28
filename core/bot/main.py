from aiogram import Dispatcher, Bot

from .handlers.scrapper import router as scrapper_router
from .handlers.commands import router as command_router


async def bot_start(token: str):
    bot = Bot(token)
    dp = Dispatcher()
    
    dp.include_routers(scrapper_router, command_router)
    await dp.start_polling(bot)