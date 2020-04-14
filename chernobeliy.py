import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
#Что ты тут забыл?
@borg.on(admin_cmd("wb ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Ответь на сообщение пользователя```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Эммм, а на фото ты отвечать не пробовал(а)?```")
       return
    chat = "@photocolorizerbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Ответь  сообщение РЕАЛЬНОГО ПОЛЬЗОВАТЕЛЯ с фото```")
       return
    await event.edit("```В процессе```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1072675522))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Запустите @photocolorizerbot и попробуйте снова```")
              return
          if response.text.startswith("😊"):
             await event.edit("```Пожалуйста ОТКЛЮЧИТЕ настройки конфиденциальности для пересылки.```")
          else: 
             await borg.forward_messages(event.chat_id, response.message)
