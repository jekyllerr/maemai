import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from routers.rp import rp_router
from routers.admin import admin_router
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(rp_router)
dp.include_router(admin_router)

# webhook handler для Яндекс.Облако
async def handler(event, context):
    update = Update.from_dict(event)
    await dp.process_update(update)
    return {"statusCode": 200, "body": "ok"}

# Для локальной отладки через polling
if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
