"""команда: .obmen usd rub"""
from telethon import events
import asyncio
from datetime import datetime
import requests
from uniborg.util import admin_cmd


@borg.on(admin_cmd("obmen (.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            nomer = float(input_sgra[0])
            val1 = input_sgra[1].upper()
            val2 = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(val1)
            otvet = requests.get(request_url).json()
            if val2 in otvet["rates"]:
                current_rate = float(otvet["rates"][val2])
                rebmun = round(nomer * current_rate, 2)
                await event.edit("{} {} = {} {}".format(nomer, val1, rebmun, val2))
            else:
                await event.edit("НИЧЕГО НЕ ПОНИМАЮ")
        except e:
            await event.edit(str(e))
    else:
        await event.edit("`.obmen -число- -из- -в-`")
    end = datetime.now()
    ms = (end - start).seconds
