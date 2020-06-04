"""Получаем Астрономическое фото дня (Astronomy Picture of the Day), может потом добавлю архив
Написал Айвен, https://github.com/AivenGog/ftg, кто удалит, тот плохой человек, неуважающий труд других
Синтаксис: .apod  """

import time
from uniborg.util import admin_cmd
from telethon import events
import requests
from googletrans import Translator


@borg.on(events.NewMessage(pattern=r"\.apod", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    response_api = requests.get("https://api.nasa.gov/planetary/apod?api_key=YDNm230oBE5IQdDenyQCzB5P62Hhc9EAJcLxKHE3").json()
    title = translator.translate(response_api["title"], dest='ru')
    opis = translator.translate(response_api["explanation"], dest='ru')
    await event.edit(
            """
**Дата**: {} 
**Название**: {}


`Описание`: {}


**Ссылка (в Сибирь)**: {}
Главный космонавт: @aivengog
            """.format(
                response_api["date"],
                title,
                opis,
                response_api["url"]
                      )

                     )
    #Ты заблудился?) пишет Айвен, не удаляй. Дальше будет больше модулей!
