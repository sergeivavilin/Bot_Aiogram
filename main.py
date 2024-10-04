import asyncio

from aiogram import Bot, Dispatcher, Router, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from  aiogram.types import Message
from decouple import config


bot = Bot(token=config("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())