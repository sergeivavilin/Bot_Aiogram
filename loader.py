from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config

# TODO Добавить логирование и базу данных
# Создаем бота, токен берем из файла config
bot = Bot(token=config("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# инициализируем диспатчер
dp = Dispatcher(storage=MemoryStorage())
