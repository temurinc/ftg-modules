# -*- coding: future_fstrings -*-

#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2020 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
import requests
import json
from datetime import datetime
import dateutil.parser

from .. import utils

def register(cb):
    cb(CoronaReportsMod())
    async def coronacmd(self, message):
        """.covid <Страна (или нет, тогда выведет указанную)>"""
        args = utils.get_args_raw(message)
        if not args:
            country = "UZ"
        else:
            country = args

        await message.edit("<code>Надеваем маску...</code>")

        url = "https://covid19.mathdro.id/api/countries/"{"name":"Uzbekistan","iso2":"UZ","iso3":"UZB"}
        tries = 0
        response = requests.get(url)

        while response.status_code == 400 and tries < 10:
            response = requests.get(url)
            tries += 1
            await message.edit("<code>Попробуй #" + str(tries) + "...</code>")

        jsonDumps = json.dumps(response.json(), sort_keys=True)
        jsonResponse = json.loads(jsonDumps)

        if(response.status_code == 200):
            confirmed = jsonResponse['confirmed']['value']
            recovered = jsonResponse['recovered']['value']
            deaths = jsonResponse['deaths']['value']
            active = confirmed - recovered - deaths

            try:
                lastUpdate = dateutil.parser.parse(jsonResponse['lastUpdate']).strftime("%d/%m/%Y \n Информация о стране обновлена в %X часов")
            except (ValueError, TypeError) as e:
                logger.error(e)
                lastUpdate = jsonResponse['lastUpdate']

            msg = "<s>--------------------------------------------------------</s>\n";
            msg += "👑🦠 в "+ country.capitalize() + "<i> "+lastUpdate+"</i>\n"
            msg += "<s>--------------------------------------------------------</s>\n";
            msg+= "<b>😷 Подтвержденые случаи:</b> " + str(confirmed)
            msg+= "\n<b>🤧 Тяжело больные:</b> " + str(active) + " (" + str(round(active/confirmed * 100, 2)) + "%)"
            msg+= "\n<b>🏥 Выздоровевшие:</b> " + str(recovered) + " (" + str(round(recovered/confirmed * 100, 2)) + "%)"
            msg+= "\n<b>💀 Умершие:</b> " + str(deaths) + " (" + str(round(deaths/confirmed * 100, 2)) + "%)"


        elif response.status_code == 404:
            msg = "<code>"+jsonResponse['error']['message']+"</code>"
        elif response.status_code == 400:
            msg = "<code>Ошибка 400, вызов неизвестного для системы (Нео очнись) идентификатора страны или ещё какая ошибка ввода</code>"
        else:
            msg = "<code>Неизвестная ошибка, наверное инопланетяне перехватывают сигнал)</code>"
        await message.edit(msg)
