from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Bot_States.States import UserState

from keyboards.all_keyboards import inline_kb

base_router = Router()
# Отлавливаем сообщения с текстом "рассчитать" и отправляем inline клавиатуру
@base_router.message(F.text.lower().contains("рассчитать"))
async def inline_menu(message: Message):
    await message.answer(f"Выберите опцию: ", reply_markup=inline_kb.as_markup(resize_keyboard=True))


# Отлавливаем callback сообщения с текстом "calories"
# Теперь у магического фильтра F мы должны использовать data вместо text
@base_router.callback_query(F.data.contains("formulas"))
async def get_formulas(call: CallbackQuery):
    await call.message.answer(text=f"10 x вес(кг) + 6.25 x рост(см) - 5 x возраст(лет) - 161")


# Отлавливаем callback сообщения с текстом "calories"
@base_router.callback_query(F.data.contains("calories"))
async def set_age(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f"Введите свой возраст: ")
    # Переводим пользователя в следующее состояние
    await state.set_state(UserState.age)


@base_router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(age=message.text)
    await message.answer(f"Введите свой рост: ")
    # Переводим пользователя в следующее состояние
    await state.set_state(UserState.growth)


@base_router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(growth=message.text)
    await message.answer(f"Введите свой вес: ")
    # Переводим пользователя в следующее состояние
    await state.set_state(UserState.weight)


@base_router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    # Сохраняем данные пользователя
    await state.update_data(weight=message.text)
    # получаем все данные пользователя в виде словаря
    data = await state.get_data()
    # вычисляем норму калорий
    man_calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5
    await message.answer(f"Ваша норма калорий: {man_calories} ккал")
    # Сбрасываем состояния пользователя
    await state.clear()


# Если оставить роутер без аргументов, то он будет отлавливать все необработанные ранее сообщения
@base_router.message()
async def all_massages(message: Message):
    await message.answer(f"Введите команду /start, чтобы начать общение.")
