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
async def handle_webhook(request: web.Request):
    data = await request.json()
    update = Update.parse_obj(data)
    # В Aiogram 3.x правильно так:
    await dp.feed_update(update)
    return web.Response(text="ok")

app = web.Application()
app.router.add_post("/", handle_webhook)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    logging.info(f"Running on port {port}")
    web.run_app(app, host="0.0.0.0", port=port)
