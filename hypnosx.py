from telethon import events

import asyncio

import os

import sys

@borg.on(events.NewMessage(pattern=r"\.hypnos", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    await event.edit("OOOOOOO \nOOOOOOO \nOOOOOOO \nOOOOOOO \nOOOOOOO \nOOOOOOO \nOOOOOOO \n")
    await asyncio.sleep(0.3)
    await event.edit("OOOOOOO \nOOOOOOO \nOOOOOOO \nOOO#OOO \nOOOOOOO \nOOOOOOO \nOOOOOOO \n")
    await asyncio.sleep(0.3)
    await event.edit("OOOOOOO \nOOOOOOO \nOO###OO \nOO#O#OO \nOO###OO \nOOOOOOO \nOOOOOOO \n")
    await asyncio.sleep(0.3)
    await event.edit("OOOOOOO \nOOOOOOO \nOO###OO \nOO#O#OO \nOO###OO \nOOOOOOO \nOOOOOOO \n")
    await asyncio.sleep(0.3)
    await event.edit("####### \n#OOOOO# \n#OOOOO# \n#OOOOO# \n#OOOOO# \n#OOOOO# \n####### \n")
    await asyncio.sleep(0.3)
    await event.edit("#O#O#O#O \nO#O#O#O# \n#O#O#O#O \nO#O#O#O# \n#O#O#O#O \nO#O#O#O# \n#O#O#O#O \nO#O#O#O# \n")
    await asyncio.sleep(0.3)
    await event.edit("O#O#O#O# \n#O#O#O#O \nO#O#O#O# \n#O#O#O#O \nO#O#O#O# \n#O#O#O#O \nO#O#O#O# \n#O#O#O#O \n")
    await asyncio.sleep(0.3)
    await event.edit("OOOOOOO \nO#####O \nO#OOO#O \nO#O#O#O \nO#OOO#O \nO#####O \nOOOOOOO \n")
    await asyncio.sleep(0.3)
    await event.edit("####### \n#OOOOO# \n#O###O# \n#O#O#O# \n#O###O# \n#OOOOO# \n####### \n")
    await asyncio.sleep(0.3)
    await event.edit("OOOOOOO \nO#####O \nO#OOO#O \nO#O#O#O \nO#OOO#O \nO#####O \nOOOOOOO \n")
    await asyncio.sleep(0.3)
    await event.edit("####### \n#OOOOO# \n#O###O# \n#O#O#O# \n#O###O# \n#OOOOO# \n####### \n")
    await asyncio.sleep(0.3)
    await event.edit("OOOOOOO \nO#####O \nO#OOO#O \nO#O#O#O \nO#OOO#O \nO#####O \nOOOOOOO \n")
    await asyncio.sleep(0.3)
    await event.edit("##### \n#OOO# \n#O#O# \n#OOO# \n##### \n")
    await asyncio.sleep(0.3)
    await event.edit("##### \n#OOO# \n#O#O# \n#OOO# \n##### \n")                 
