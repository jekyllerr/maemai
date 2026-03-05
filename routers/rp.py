from uuid import uuid4
from aiogram import Router, types, F
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    MessageEntity,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from aiogram import Router

rp_router = Router()
requests = {}

# RP-команды
rp_commands = [
    {
        "title": "Кочакланышырга",
        "case": "possesive",
        "description": "Әңгәмәдәш белән кочакланышырга",
        "thumb_url": "https://i.pinimg.com/736x/c0/98/ad/c098ad1a516843395c99039def9da66f.jpg",
        "message_text": "{user}{user_suffix} кочакланышасы килә",
        "accept_text": "{user1} {user2} белән кочакланышты",
        "emoji_id": "5258417246056754328"
    },
    {
        "title": "Башыңнан сыйпарга",
        "case": "possessive",
        "description": "Әңгәмәдәшнең башыннан сыйпарга",
        "thumb_url": "https://i.pinimg.com/736x/21/fb/d2/21fbd2226daa89d323c4581ae112c240.jpg",
        "message_text": "{user}{user_suffix} башыңнан сыйпыйсы килә",
        "accept_text": "{user1} {user2}{user2_suffix} башыңнан сыйпады",
        "emoji_id": "5190923814980045139"
    },
    {
        "title": "Кыйнарга",
        "case": "accusative",
        "description": "Әңгәмәдәшне кыйнарга",
        "thumb_url": "https://i.pinimg.com/736x/60/c2/80/60c2806881ff18faf834da9cbddb02b2.jpg",
        "message_text": "{user}{user_suffix} кыйныйсы килә",
        "accept_text": "{user1} {user2}{user2_suffix} кыйнады",
        "emoji_id": "5260636717651603317"
    },
    {
        "title": "Гаепле итәргә",
        "case": "accusative",
        "description": "Әңгәмәдәшне гаепле итәргә",
        "thumb_url": "https://i.pinimg.com/736x/fd/20/d4/fd20d45c9620841960fc1c10885ea4c1.jpg",
        "message_text": "{user}{user_suffix} гаепле итәсе килә",
        "accept_text": "{user1} {user2}{user2_suffix} гаепле итте",
        "emoji_id": "5258503463230253720"
    },
    {
        "title": "Сугышырга",
        "description": "Әңгәмәдәш белән сугышырга",
        "thumb_url": "https://i.pinimg.com/736x/92/54/8e/92548e09176d3ea2f780c32cb97db99e.jpg",
        "message_text": "{user}{user_suffix} сугышасы килә",
        "accept_text": "{user1} {user2} белән сугышты",
        "emoji_id": "5361597229683449359"
    },
    {
        "title": "Кунакка чакырырга",
        "case": "accusative",
        "description": "Әңгәмәдәшне кунакка чакырырга",
        "thumb_url": "https://i.pinimg.com/736x/67/b9/3f/67b93f5e8576918194be9e37bed91c73.jpg",
        "message_text": "{user}{user_suffix} кунакка чакырасы килә",
        "accept_text": "{user1} {user2}{user2_suffix} кунакка чакырды",
        "emoji_id": "5260681054598999309"
    },
    {
        "title": "Кутакка утыртырга",
        "case": "accusative",
        "description": "Әңгәмәдәшне кутакка утыртырга",
        "thumb_url": "https://i.pinimg.com/736x/ec/63/8f/ec638fc2fb82ae17518275daceaaf7e0.jpg",
        "message_text": "{user}{user_suffix} кутакка утырасы килә",
        "accept_text": "{user1} {user2}{user2_suffix} кутакка утырткан",
        "emoji_id": "5362034865376073854"
    },
    {
        "title": "Бәрергә",
        "case": "accusative",
        "description": "Әңгәмәдәшкә бәрергә",
        "thumb_url": "https://i.pinimg.com/736x/30/25/73/302573f26ec8d602ae8ba3c3f4432558.jpg",
        "message_text": "{user}{user_suffix} бәрәсе килә",
        "accept_text": "{user1} {user2}{user2_suffix} бәрде",
        "emoji_id": "5258494826051021952"
    }, 
    {
        "title": "Сегәргә",
        "case": "accusative",
        "description": "Әңгәмәдәшне сегәргә",
        "thumb_url": "https://i.pinimg.com/736x/73/b8/98/73b898b6553603a95765619bd5978726.jpg",
        "message_text": "{user}{user_suffix} сегәсе килә",
        "accept_text": "{user1} {user2}{user2_suffix} секте",
        "emoji_id": "5258145658094757763"
    },
    {
        "title": "Көчләргә",
        "case": "accusative",
        "description": "Әңгәмәдәшне көчләргә",
        "thumb_url": "https://i.pinimg.com/736x/d9/b0/71/d9b07129102394be1d9e77941dd32b74.jpg",
        "message_text": "{user}{user_suffix} көчлисе килә",
        "accept_text": "{user1} {user2}{user2_suffix} көлчәдә",
        "emoji_id": "5258200530596932833"
    },
    {
        "title": "Бәйләргә",
        "case": "accusative",
        "description": "Әңгәмәдәшне бәйләргә",
        "thumb_url": "https://i.pinimg.com/1200x/f2/8c/fd/f28cfda4ed89af625a5c001004dfe42b.jpg",
        "message_text": "{user}{user_suffix} бәйлисе килә",
        "accept_text": "{user1} {user2}{user2_suffix} бәйледә",
        "emoji_id": "5258360608323021231"
    },
    {
        "title": "Мәҗбүр итәргә",
        "case": "accusative",
        "description": "Әңгәмәдәшне мәҗбүр итәргә",
        "thumb_url": "https://i.pinimg.com/1200x/cb/70/32/cb7032bf5306c7a6c4abbc03f114f12c.jpg",
        "message_text": "{user}{user_suffix} мәҗбүр итәсе килә",
        "accept_text": "{user1} {user2}{user2_suffix} мәҗбүр итте",
        "emoji_id": "5258307084440580039"
    },
    {
        "title": "Асырга",
        "case": "accusative",
        "description": "Әңгәмәдәшне асырга",
        "thumb_url": "https://i.pinimg.com/1200x/a9/19/85/a9198533d559ddc0d6f0b972fca1c98c.jpg",
        "message_text": "{user}{user_suffix} асасы килә",
        "accept_text": "{user1} {user2}{user2_suffix} асты",
        "emoji_id": "5258307084440580039"
    },
    {
        "title": "Юк итәргә",
        "case": "accusative",
        "description": "Әңгәмәдәшне юк итәргә",
        "thumb_url": "https://i.pinimg.com/1200x/0f/e8/76/0fe87604a8aab6eea487bd8cfa825c28.jpg",
        "message_text": "{user}{user_suffix} юк итәсе килә",
        "accept_text": "{user1} {user2}{user2_suffix} юк итте",
        "emoji_id": "5298907281440643579"
    },
    {
        "title": "Сатарга",
        "case": "accusative",
        "description": "Әңгәмәдәшне сатарга",
        "thumb_url": "https://i.pinimg.com/736x/bd/b9/4f/bdb94f56d0ff74a8a3d1f2748d69921a.jpg",
        "message_text": "{user}{user_suffix} сатасы килә",
        "accept_text": "{user1} {user2}{user2_suffix} сатты",
        "emoji_id": "5240290577102152084"
    },
    {
        "title": "Кытыкларга",
        "case": "accusative",
        "description": "Әңгәмәдәшне кытыкларга",
        "thumb_url": "https://i.pinimg.com/736x/80/58/18/805818f643f8de1a04c6a5977adcf901.jpg",
        "message_text": "{user}{user_suffix} кытыклыйсы килә",
        "accept_text": "{user1} {user2}{user2_suffix} кытыклады",
        "emoji_id": "5230932994415404463"
    },
    {
        "title": "Шартларга",
        "case": "accusative",
        "description": "Әңгәмәдәшне шартларга",
        "thumb_url": "https://i.pinimg.com/736x/ee/3a/38/ee3a381a1c9efcde170fd28ab861f332.jpg",
        "message_text": "{user}{user_suffix} шартлыйсы килә",
        "accept_text": "{user1} {user2}{user2_suffix} шартлады",
        "emoji_id": "5337164002550097692"
    },
    {
        "title": "Атарга",
        "case": "accusative",
        "description": "Әңгәмәдәшне мылтыктан атарга",
        "thumb_url": "https://tse1.explicit.bing.net/th/id/OIP.ZaTYcJXfo8bSZId1sMi2HgAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",
        "message_text": "{user}{user_suffix} мылтыктан атыйсы килә",
        "accept_text": "{user1} {user2}{user2_suffix} мылтыктан атты",
        "emoji_id": "5197253492967743921"
    },
    {
        "title": "Үбешергә",
        "description": "Әңгәмәдәшне үбәргә",
        "thumb_url": "https://i.pinimg.com/1200x/57/f5/78/57f578c6e13257e30873c7d649732a03.jpg",
        "message_text": "{user}{user_suffix} үбешәсе килә",
        "accept_text": "{user1} {user2}{user2_suffix} белән үбеште",
        "emoji_id": "5190818425072534085"
    },
    {
        "title": "Ятарга",
        "description": "Әңгәмәдәш яныңа яткырырга",
        "thumb_url": "https://i.pinimg.com/736x/42/af/09/42af0918ddfaaf26462805a93f7e26f6.jpg",
        "message_text": "{user}{user_suffix} яныңа ятасы килә",
        "accept_text": "{user1} {user2} янына ятты",
        "emoji_id": "5370831009937890906"
    },
    {
        "title": "Хурларга",
        "case": "accusative",
        "description": "Әңгәмәдәшне хурларга",
        "thumb_url": "https://i.pinimg.com/736x/f8/41/eb/f841eb0605f6c8a93176c5960dc0fc9e.jpg",
        "message_text": "{user}{user_suffix} хурлыйсы килә",
        "accept_text": "{user1} {user2}{user2_suffix} хурлады",
        "emoji_id": "5361597229683449359"
    },
    {
        "title": "Уңышлар теләргә",
        "case": "dative",
        "description": "Әңгәмәдәшкә уңышлар теләргә",
        "thumb_url": "https://i.pinimg.com/736x/d0/4b/41/d04b412a3c2596572b65ec57237f1908.jpg",
        "message_text": "{user}{user_suffix} уңышлар телисе килә",
        "accept_text": "{user1} {user2}{user2_suffix} уңышлар теләде",
        "emoji_id": "5195111279244619776"
    },
    {
        "title": "Суырырга",
        "case": "from",
        "description": "Әңгәмәдәшне суырырга",
        "thumb_url": "https://i.pinimg.com/1200x/17/4b/ff/174bff1f21668f79fbd7af8b39ee8147.jpg",
        "message_text": "{user}{user_suffix} суырасы килә",
        "accept_text": "{user1} {user2}{user2_suffix} суырды",
        "emoji_id": "5260557290821396957"
    },
    {
        "title": "Яларга",
        "case": "from",
        "description": "Әңгәмәдәшне яларга",
        "thumb_url": "https://i.pinimg.com/736x/61/5b/0c/615b0cf1ec0b571b955251bb6c19b18b.jpg",
        "message_text": "{user}{user_suffix} ялыйсы килә",
        "accept_text": "{user1} {user2}{user2_suffix} ялады",
        "emoji_id": "5260516943898620211"
    }
]

from aiogram import Router, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, MessageEntity, InlineQueryResultArticle, InputTextMessageContent
from uuid import uuid4

requests = {}

# Функция для суффиксов
def get_suffix(name: str, case: str = "accusative") -> str:
    """Возвращает суффикс для татарских имён по падежу"""
    last_char = name[-1].lower()
    
    # possessive (-нең/-ның)
    if case == "possessive":
        return "нең" if last_char in "мн" else "ның"
    
    # dative (-кә/-гә)
    elif case == "dative":
        return "гә" if last_char in "нг" else "кә"
    
    # accusative (-не/-ны)
    elif case == "accusative":
        return "не" if last_char in "нг" else "ны"
    
    # from (-дан/-дән)
    elif case == "from":
        return "дән" if last_char in "мн" else "дан"
    
    return ""

def utf16_len(s: str) -> int:
    return len(s.encode('utf-16-le')) // 2

def utf16_offset(text: str, substring: str) -> int:
    prefix = text[:text.find(substring)]
    return utf16_len(prefix)

@rp_router.message() 
async def start_message(message: types.Message):
    if message.text == "/start": 
        await message.answer( 
            "<b>Ботны ничек кулланырга?</b>\n\n" 
            "1. @MaemaiBot шәхси хәбәрләрендә яз һәм исемлектән гамәлне сайла!\n" 
            "2. Башка кулланучы гамәлне кабул итәргә яки кире кагарга тиеш!\n" 
            "3. Пёрррфект!", 
            parse_mode="HTML" 
        )
    

# ----- inline RP handler -----
@rp_router.inline_query()
async def inline_rp_handler(query: types.InlineQuery):
    user = query.from_user
    user_name = user.full_name

    results = []

    for action in rp_commands:
        request_id = str(uuid4())
        request_data = {
            "id": request_id,
            "initiator_id": user.id,
            "initiator_name": user_name,
            "title": action["title"],
            "message_text": action["message_text"],
            "accept_text": action["accept_text"],
            "emoji_id": action["emoji_id"],
            "case": action.get("case", "accusative"),  # ← ВОТ ЭТО ДОБАВЬ
            "status": "pending",
            "thumb_url": action.get("thumb_url")
        }
        requests[request_id] = request_data
        
        # Выбираем правильный суффикс
        case_type = action.get("case", "accusative")
        user_suffix = get_suffix(user_name, case=case_type)

        # Формируем текст: кастомный emoji в начале текста
        message_body = action["message_text"].format(
            user=user_name,
            user_suffix=user_suffix
        )
        
        message_text = f"  💭 | {message_body}"  # кастомный emoji

        # UTF-16 оффсет для кликабельного имени
        def utf16_offset(text, sub):
            return len(text[:text.find(sub)].encode('utf-16-le')) // 2

        def utf16_len(text):
            return len(text.encode('utf-16-le')) // 2

        name_offset = utf16_offset(message_text, user_name)
        name_length = utf16_len(user_name)

        entities = [
            MessageEntity(
                type="custom_emoji",
                offset=0,              # emoji в самом начале
                length=2,              # кастомный emoji = 2 UTF-16
                custom_emoji_id=action["emoji_id"]
            ),
            MessageEntity(
                type="text_link",
                offset=name_offset,
                length=name_length,
                url=f"tg://user?id={user.id}"
            )
        ]

        # Inline клавиатура
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[ 
                InlineKeyboardButton(
                    text="✅ Кабул ит",
                    callback_data=f"accept:{request_id}"
                ),
                InlineKeyboardButton(
                    text="❌ Баш тарт",
                    callback_data=f"decline:{request_id}"
                )
            ]]
        )

        # Добавляем результат в список
        results.append(
            InlineQueryResultArticle(
                id=request_id,
                title=action["title"],
                description=action.get("description", ""),
                input_message_content=InputTextMessageContent(
                    message_text=message_text,
                    entities=entities
                ),
                reply_markup=keyboard,
                thumb_url=action.get("thumb_url")
            )
        )

    await query.answer(results, cache_time=0)

# ----- accept handler -----
@rp_router.callback_query(F.data.startswith("accept:"))
async def accept_handler(callback: types.CallbackQuery):
    request_id = callback.data.split(":")[1]
    request_data = requests.get(request_id)
    if not request_data:
        await callback.answer("Тәкъдим табылмады.", show_alert=True)
        return
    if request_data["initiator_id"] == callback.from_user.id:
        await callback.answer("Кем үз-үзен рп-лап утыра монда?", show_alert=True)
        return
    if request_data["status"] != "pending":
        await callback.answer("Бу RP тәмамланган иде.", show_alert=True)
        return

    request_data["status"] = "accepted"

    user1_id = request_data["initiator_id"]
    user1_name = request_data["initiator_name"]

    user2 = callback.from_user
    user2_id = user2.id
    user2_name = user2.full_name

    case_type = request_data.get("case", "accusative")
    user2_suffix = get_suffix(user2_name, case=case_type)

    final_text = request_data["accept_text"].format(
        user1=user1_name,
        user2=user2_name,
        user2_suffix=user2_suffix
)

    # Добавляем эмодзи в начале
    text = f"🫧 | {final_text}"

    # Определяем, как user2 реально выглядит в тексте
    if "{user2_suffix}" in request_data["accept_text"]:
        user2_text = f"{user2_name}{user2_suffix}"
    else:
        user2_text = user2_name

    entities = [
        MessageEntity(
            type="custom_emoji",
            offset=0,
            length=2,
            custom_emoji_id=request_data["emoji_id"]
        ),
        MessageEntity(
            type="text_link",
            offset=utf16_offset(text, user1_name),
            length=utf16_len(user1_name),
            url=f"tg://user?id={user1_id}"
        ),
        MessageEntity(
            type="text_link",
            offset=utf16_offset(text, user2_text),
            length=utf16_len(user2_text),
            url=f"tg://user?id={user2_id}"
        )
    ]

    try:
        if callback.inline_message_id:
            await callback.bot.edit_message_text(
                inline_message_id=callback.inline_message_id,
                text=text,
                entities=entities
            )
        else:
            await callback.message.edit_text(
                text=text,
                entities=entities
            )
    except Exception as e:
        print("Хата accept:", e)

    requests.pop(request_id, None)
    await callback.answer()

# ----- decline handler -----
@rp_router.callback_query(F.data.startswith("decline:"))
async def decline_handler(callback: types.CallbackQuery):
    request_id = callback.data.split(":")[1]
    request_data = requests.get(request_id)
    if not request_data:
        await callback.answer("Тәкъдим табылмады.", show_alert=True)
        return
    if request_data["initiator_id"] == callback.from_user.id:
        await callback.answer("Кем үз-үзен рп-лап утыра монда?", show_alert=True)
        return

    request_data["status"] = "declined"
    user1_id = request_data["initiator_id"]
    user1_name = request_data["initiator_name"]
    user1_suffix = get_suffix(user1_name)

    user2 = callback.from_user
    user2_id = user2.id
    user2_name = user2.full_name

    text = f"❌ | {user2_name} {user1_name}{user1_suffix} тәкъдимен кире какты"

    entities = [
        MessageEntity(
            type="text_link",
            offset=utf16_offset(text, user1_name),
            length=utf16_len(user1_name),
            url=f"tg://user?id={user1_id}"
        ),
        MessageEntity(
            type="text_link",
            offset=utf16_offset(text, user2_name),
            length=utf16_len(user2_name),
            url=f"tg://user?id={user2_id}"
        )
    ]

    try:
        if callback.inline_message_id:
            await callback.bot.edit_message_text(
                inline_message_id=callback.inline_message_id,
                text=text,
                entities=entities
            )
        else:
            await callback.message.edit_text(
                text=text,
                entities=entities
            )

    except Exception as e:
        print("Хата decline:", e)

    requests.pop(request_id, None)
    await callback.answer()

