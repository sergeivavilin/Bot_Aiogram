import asyncio

from loader import bot, dp
from handlers.start import start_router
from handlers.base_handlers import base_router


# Основная асинхронная функция. Добавляем роутер в диспатчер и запускаем его.
async def main():
    dp.include_router(start_router)
    dp.include_router(base_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
