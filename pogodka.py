#Получаем погодку с помощью OpenWeatherMap
#Что писать: .pogoda <Место поиска> 
 
import aiohttp
import time
from datetime import tzinfo, datetime
from uniborg.util import admin_cmd
 
 
@borg.on(admin_cmd("pogoda (.*)"))
async def _(event):
    if event.fwd_from:
        return
    sample_url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"
    input_str = event.pattern_match.group(1)
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(input_str, Config.OPEN_WEATHER_MAP_APPID))
    response_api = await response_api_zero.json()
    if response_api["cod"] == 200:
        country_code = response_api["sys"]["country"]
        country_time_zone = int(response_api["timezone"])
        sun_rise_time = int(response_api["sys"]["sunrise"]) + country_time_zone
        sun_set_time = int(response_api["sys"]["sunset"]) + country_time_zone
        await event.edit(
            """{}
**🌡️Температура**: {}°С
    __минимальная__: {}°С
    __максимальная__ : {}°С
**🌪️Влажность**: {}%
**🌬️Скорость ветра**: {}м/с
**☁️Давление**: {}Паскаль
**🌞Рассвет**: {} {}
**🌟Закат**: {} {}""".format(
                input_str,
                response_api["main"]["temp"],
                response_api["main"]["temp_min"],
                response_api["main"]["temp_max"],
                response_api["main"]["humidity"],
                response_api["wind"]["speed"],
                response_api["clouds"]["all"],
                # response_api["main"]["pressure"],
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_rise_time)),
                country_code,
                time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(sun_set_time)),
                country_code
            )
        )
    else:
        await event.edit(response_api["message"])
