import os
import logging
from aiohttp import web
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

# Обработчик вебхука
async def handle_webhook(request):
    data = await request.json()
    update = Update.parse_obj(data)
    await dp.process_update(update)
    return web.Response(text="ok")

# Создаем приложение aiohttp
app = web.Application()
app.router.add_post("/", handle_webhook)  # Вебхук Telegram отправляет POST на "/"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render использует переменную PORT
    logging.info(f"Running on port {port}")
    web.run_app(app, host="0.0.0.0", port=port)
