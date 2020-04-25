from telethon import events
import asyncio
import os
import sys
from uniborg import util


@borg.on(util.admin_cmd(pattern="rt ?(.*)"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    b = ' '
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*18, paytext*18, b*7 + paytext * 4, b*7 + paytext * 4, b*7 + paytext * 4, b*7 + paytext * 4, b*7 + paytext * 4, b*7 + paytext * 4, b*7 + paytext * 4, b*7 + paytext * 4, b*7 + paytext * 4, b*7 + paytext * 4, )
    await event.edit(pay)
