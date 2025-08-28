from aiogram import Dispatcher, Bot

from .handlers.messages import router as message_router
from .handlers.commands import router as command_router


async def bot_start(token: str):
    bot = Bot(token)
    dp = Dispatcher()
    
    dp.include_routers(message_router, command_router)
    await dp.start_polling(bot)