import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram.types import Message
from aiogram.filters import CommandStart

# Для хранения и настройки чувствительных данных используем библиотеку decouple
# Можно использовать dotenv или просто переменные окружения для хранения токена
from decouple import config

# Создаем бота, токен берем из файла .env
bot = Bot(token=config("BOT_TOKEN"))
# инициализируем диспатчер
dp = Dispatcher(storage=MemoryStorage())
# Создаем базовый роутер (в версии 3.x используется Router() вместо dp.message_handler)
base_router = Router()

# Класс CommandStart обрабатывает только команду /start.
@base_router.message(CommandStart())
async def start(message: Message):
    print(f"Привет! {message.from_user.full_name}! Я бот помогающий твоему здоровью.")

# Если оставить роутер без аргументов, то он будет отлавливать все необработанные ранее сообщения
@base_router.message()
async def all_massages(message: Message):
    print(f"Введите команду /start, чтобы начать общение.")

# Основная асинхронная функция. Добавляем роутер в диспатчер и запускаем его.
async def main():
    dp.include_router(base_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
