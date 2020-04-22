import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
#Что ты тут забыл?
@borg.on(admin_cmd("story ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Ответь на сообщение пользователя```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Эммм, а на текст ты отвечать не пробовал(а)?```")
       return
    chat = "@HistoryAIBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Ответь  сообщение РЕАЛЬНОГО ПОЛЬЗОВАТЕЛЯ```")
       return
    await event.edit("```В процессе```")
    await event.delete()
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1045054453))
              await borg.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Запустите @HistoryAIBot и попробуйте снова```")
              return
          if response.text.startswith("Привет, я дополню твою историю при помощи нейросети."):
             await event.edit("```Пожалуйста ОТКЛЮЧИТЕ настройки конфиденциальности для пересылки.```")
          else: 
             await borg.forward_messages(event.chat_id, response.message)
