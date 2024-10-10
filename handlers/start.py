from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.all_keyboards import kb

start_router = Router()

# Класс CommandStart обрабатывает только на команду /start.
@start_router.message(CommandStart())
async def start(message: Message):
    # При вводе команды /start отправляем клавиатуру, которая будет подстраиваться под размеры интерфейса
    await message.answer(
        text=f"Привет! {message.from_user.full_name}! Я бот помогающий твоему здоровью.",
        reply_markup=kb.as_markup(resize_keyboard=True,one_time_keyboard=True)
    )
