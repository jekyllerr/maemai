import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from routers.rp import rp_router
from routers.admin import admin_router
from aiohttp import web

# Логирование
logging.basicConfig(level=logging.INFO)

# Токен бота
API_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(rp_router)
dp.include_router(admin_router)

# Обработчик webhook
async def handle_webhook(request):
    if request.method == "POST":
        try:
            data = await request.json()
            update = Update.from_dict(data)
            await dp.process_update(update)
        except Exception as e:
            logging.exception("Ошибка при обработке обновления")
        return web.json_response({"status": "ok"})
    # Для GET / возвращаем просто текст, чтобы Render или браузер не ругались
    return web.Response(text="Bot is running", status=200)

# Создаём aiohttp приложение и добавляем маршрут
app = web.Application()
app.router.add_route("*", "/", handle_webhook)

# Запуск сервера
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render задаёт PORT
    logging.info(f"Starting webhook server on 0.0.0.0:{port}")
    web.run_app(app, host="0.0.0.0", port=port)
