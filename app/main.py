import asyncio
import os

from bot.main import bot_start

from dotenv import load_dotenv
from config import env_path

load_dotenv(dotenv_path=env_path)
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def main():
    await bot_start(TELEGRAM_BOT_TOKEN)

if __name__ == '__main__':
    asyncio.run(
        main()
    )