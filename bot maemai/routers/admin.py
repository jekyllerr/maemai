from aiogram import Router, types, F
from aiogram.filters import Command

admin_router = Router()

# Хранилище ролей (пока в памяти)
roles = {
    "owner": 410172741,
    "admins": set(),
    "managers": set()
}

# ---- Проверки ----

def is_owner(user_id: int) -> bool:
    return user_id == roles["owner"]

def is_admin(user_id: int) -> bool:
    return user_id in roles["admins"] or is_owner(user_id)

def is_manager(user_id: int) -> bool:
    return user_id in roles["managers"] or is_admin(user_id)

@admin_router.message(Command("add_admin"))
async def add_admin_handler(message: types.Message):
    if not is_owner(message.from_user.id):
        return await message.answer("Только владелец может назначать админов.")

    if not message.reply_to_message:
        return await message.answer("Ответьте на сообщение пользователя.")

    user_id = message.reply_to_message.from_user.id
    roles["admins"].add(user_id)

    await message.answer("Админ назначен.")

    @admin_router.message(Command("remove_admin"))
    async def remove_admin_handler(message: types.Message):
     if not is_owner(message.from_user.id):
        return await message.answer("Только владелец может снимать админов.")

    if not message.reply_to_message:
        return await message.answer("Ответьте на сообщение пользователя.")

    user_id = message.reply_to_message.from_user.id
    roles["admins"].discard(user_id)

    await message.answer("Админ снят.")

    @admin_router.message(Command("admins"))
    async def list_admins_handler(message: types.Message):
     if not is_admin(message.from_user.id):
        return await message.answer("Недостаточно прав.")

    if not roles["admins"]:
        return await message.answer("Админов пока нет.")

    text = "Список админов:\n"
    for admin_id in roles["admins"]:
        text += f"- {admin_id}\n"

    await message.answer(text)