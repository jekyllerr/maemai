import os
import logging
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from routers.rp import rp_router
from routers.admin import admin_router

logging.basicConfig(level=logging.INFO)

# Токен бота из переменных окружения
API_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(rp_router)
dp.include_router(admin_router)

# Вебхук-обработчик
async def handle_webhook(request: web.Request):
    try:
        data = await request.json()
        update = Update.parse_obj(data)  # корректно создаём объект Update
        await dp.feed_update(bot=bot, update=update)  # передаём bot и update
        return web.Response(text="ok")
    except Exception as e:
        logging.exception(f"Ошибка при обработке обновления: {e}")
        return web.Response(status=500, text="error")

# Создаём aiohttp приложение
app = web.Application()
app.router.add_post("/", handle_webhook)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    logging.info(f"Запуск вебхука на порту {port}")
    web.run_app(app, host="0.0.0.0", port=port)
