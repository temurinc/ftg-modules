"""
Синтаксис: .moneta <орёл или решка> или просто, советую ставить алиас 
"""
from telethon import events
import random, re
from uniborg.util import admin_cmd


@borg.on(admin_cmd("moneta ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "решка":
            await event.edit("Монетка упала **Решкой**. \n Ура, ты угадал.")
        elif input_str == "орёл":
            await event.edit("Монетка упала **Решкой**. \n Эх, сожалею. Ты не угадал...")
        else:
            await event.edit("Монетка упала **Решкой**.")
    elif r % 2 == 0:
        if input_str == "орёл":
            await event.edit("Монетка упала **Орлом**. \n Ура, ты угадал.")
        elif input_str == "решка":
            await event.edit("Монетка упала **Орлом**. \n Эх, сожалею. Ты не угадал...")
        else:
            await event.edit("Монетка упала **Орлом**.")
    else:
        await event.edit("Поздравляю, ты разрушил законы математики.")
