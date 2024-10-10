# Создаем состояния пользователя
from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()