"""
Шлёпаем всех и вся
Команда: .shlep ответь на сообщение, а иначе модуль шлёпнет тебя).

"""

import sys
from telethon import events, functions
from uniborg.util import admin_cmd
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName


SLAP_TEMPLATES = [
    "{hits} {user2} {item}.",
    "{hits} {user2} в лицо {item}.",
    "Немного {hits} {user2} {item}.",
    "{throws} {item} в {user2}.",
    "поднимаю пакет с {item} и {throws} его на лицо {user2}.",
    "стреляю из пушки {item} в сторону {user2}.",
    "просто беру и шлёпаю {user2} {item}.",
    "прицепляю {user2} ногами к потолку и {hits} его {item}.",
    "быстро хватаю {item} и {hits} {user2} .",
    "привязываю {user2} к стулу и начинаю методично {throws}  {item} в него.",
    "подставляю плечо поддержки {user2}, а потом с прогиба кидаю в пропасть."
]

ITEMS = [
    'чугунной сковородкой',
    'большой рыбёхой',
    'бейсбольной битой',
    'деталькой от лего',
    'деревянной тростью',
    'гвоздём',
    'принтером",
    'лопатой',
    'ИВЛ-аппаратом',
    'учебником физики',
    'тостером',
    'портретом Путина',
    'телевизором',
    'пятитонным грузовиком',
    'рулоном клейкой ленты',
    'книгой',
    'клавиатурой',
    'пробегающим школьником',
    'мешком камней',
    'радужным единорогом',
    'резиновой игрушкой',
    'проводом от зарядки',
    'огнетушителем',
    'банкой варенья',
    'шаром грязи',
    'пачкой с деньгами',
    'испорченным помидором',
    'протухшим яйцом',
    'тонной кирпичей',
]

THROW = [
    "бросаю",
    "швыряю",
    "ласково кидаю",
    "метаю",
]

HIT = [
    "ударяю",
    "колочу",
    "шлёпаю",
    "размозживаю",
    "избиваю",
]
@borg.on(admin_cmd(pattern="shlep ?(.*)", allow_sudo=True))
async def who(event):
    if event.fwd_from:
        return
    replied_user = await get_user(event)
    caption = await slap(replied_user, event)
    message_id_to_reply = event.message.reply_to_msg_id

    if not message_id_to_reply:
        message_id_to_reply = None

    try:
        await event.edit(caption)

    except:
        await event.edit("`Can't slap this nibba !!`")

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`Я не шлёпаю незнакомцев !!!`")
            return None

    return replied_user

async def slap(replied_user, event):
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)

    caption = "@"+borg.me.username+" "+ temp.format(user2=slapped, item=item, hits=hit, throws=throw)

    return caption
