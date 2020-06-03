"""Получаем Астрономическое фото дня (Astronomy Picture of the Day), может потом добавлю архив
Написал Айвен, https://github.com/AivenGog/ftg, кто удалит, тот плохой человек, неуважающий труд других
Синтаксис: .apod  """

import time
from uniborg.util import admin_cmd
from telethon import events
import requests


@borg.on(events.NewMessage(pattern=r"\.apod", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    response_api = requests.get("https://api.nasa.gov/planetary/apod?api_key=YDNm230oBE5IQdDenyQCzB5P62Hhc9EAJcLxKHE3").json()
    await event.edit(
            """
**Дата**: {} 
**Название**: {}
`Описание`: {}


**Ссылка (в Сибирь)**: {}
Главный космонавт: @aivengog
            """.format(
                response_api["date"],
                response_api["title"],
                response_api["explanation"],
                response_api["url"]
                      )

                     )
    #Ты заблудился?) пишет Айвен, не удаляй. Дальше будет больше модулей!
