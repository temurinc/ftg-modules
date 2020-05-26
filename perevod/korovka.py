"""Пишем .cowsay module, Оболочка PepeBot для коровы, которая говорит разные мудрости.
    **⚠️🔞 NSFW ВНИМАНИЕ**
   +++++CREDIT+++++++
   Код : @NeoMatrix90
   Портировал @NeoMatrix90 (Ultra Legend)
   Перевёл: @aivengog
   Команда : .cowsay {text} (корова будет говорить грязные вещи. БУДЬТЕ ВНИМАТЕЛЬНЫ)) )
   		 .milksay {text} (Молочник, ненавидит корову)
   		 .tuxsay {text} (А ты сам посмотри)
   		 ну и ещё найдите, не хочу рассказывать.
   		 
   *** КАКАЯ СКОТИНА ИЗМЕНИТ ЭТОТ ТЕКСТ ТУ САМ НАЙДУ И ЗАСТАВЛЮ СЪЕСТЬ ВСЕХ ЕЁ ДЕТЕЙ. ТОЛЬКО ПОПРОБУЙ СОБАКА***
         ***🔴 НЕ КОПИРУЙТЕ БЕЗ ДИСКЛЕЙМЕРА***
         """
   
import asyncio
from telethon import events
from cowpy import cow
from uniborg.util import admin_cmd




@borg.on(events.NewMessage(pattern=r"^.(\w+)say (.*)", outgoing=True))
async def univsaye(event):
    """ .cowsay аналог (корова, которая говорит что-то.) """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        arg = event.pattern_match.group(1).lower()
        text = event.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await event.edit(f"`{cheese.milk(text).replace('`', '´')}`")
