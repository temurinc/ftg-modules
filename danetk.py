"""Немного заморочливо принимаем решение)
Команда: .danet"""
from telethon import events
import requests
from uniborg.util import admin_cmd


@borg.on(admin_cmd("danet"))
async def _(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    if r["answer"] == "yes":
        m = "ДА!"
    if r["answer"] == "no":
        m = "НЕТ!"
    await borg.send_message(
        event.chat_id,
        m,
        reply_to=message_id,
        file=r["image"]
    )
    await event.delete()
    #Зачем ты это читал?
