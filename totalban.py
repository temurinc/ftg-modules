"""Банит пользователя во всех группах, где вы админ.
Команды:
.banall Причина
.unbanall Причина"""
from telethon import events
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd("banall ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            Config.ALL_BAN_LOGGER_GROUP,
            "!забанил везде [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()


@borg.on(admin_cmd("unbanall ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            Config.ALL_BAN_LOGGER_GROUP,
            "!разбанил везде [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
