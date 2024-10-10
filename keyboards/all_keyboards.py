# Создаем клавиатуры
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

kb = ReplyKeyboardBuilder()
kb.button(text="Рассчитать")
kb.button(text="Информация")

inline_kb = InlineKeyboardBuilder()
inline_kb.button(text="Формулы расчёта", callback_data="formulas")
inline_kb.button(text="Рассчитать норму калорий", callback_data="calories")
