"""

Давай я проверю Google / YouTube / DuckDuckGo / GitHub / RBC / Xvideo / Xvideos2/ Pornhub / var / log / Dyno сециально для тебя! 

Что писать:

 .lmg <поисковый запрос Google>

 .lmy <поисковый запрос YouTube>
 
 .lmd <поисковый запрос DuckDuckGo>
 
 .lmw <поиск в Wikipedia>
 
 .lmgit <поиск репозитория в GitHub>

 .lmnews <поиск новостей>

 .lmx <поиск xvideos>
 
 .lmx2 <поиск xvideos2>

 .lmp <поиск pornhub>

 .lmvar <название приложения heroku настройки>

 .lmlog <название приложения heroku логи>

 .dyno <тип биллинга>
 



"""







from telethon import events



import os



import requests



import json



from uniborg.util import admin_cmd











@borg.on(admin_cmd(pattern="lmg (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=http://google.com/search?q={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **Google** специально для тебя:\n👉 [{}]({})\n`Лови ссылку, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")





@borg.on(admin_cmd(pattern="lmy (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.youtube.com/results?search_query={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **YouTube** специально для тебя:\n👉 [{}]({})\n`Лови ссылку, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))

#Ну вот что ты тут забыл?

    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")




@borg.on(admin_cmd(pattern="lmd (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://duckduckgo.com/?q={}&t=h_&ia=about".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **DuckDuckGo** специально для тебя:\n👉 [{}]({})\n`Лови ссылку, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")




@borg.on(admin_cmd(pattern="lmx (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.xvideos.com/?k={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **xvideo** специально для тебя:\n👉 [{}]({})\n`Не натри мозоли, и не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")




@borg.on(admin_cmd(pattern="lmp (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.pornhub.com/video/search?search={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **pornhub** специально для тебя:\n👉 [{}]({})\n`Мой совет - найди себе девушку/парня, и не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")


@borg.on(admin_cmd(pattern="lmnews (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.rbc.ua/rus/search?search_text={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **rbc** специально для тебя:\n👉 [{}]({})\n`Лови ссылку, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")



@borg.on(admin_cmd(pattern="lmvar (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/settings".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **var** специально для тебя:\n👉 [{}]({})\n`Лови ссылку, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")



@borg.on(admin_cmd(pattern="lmlog (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/apps/{}/logs".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **log** специально для тебя:\n👉 [{}]({})\n`Лови ссылку, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")

        
        
@borg.on(admin_cmd(pattern="lmx2 (.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://www.xvideos2.com/?k={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **xvideos2** специально для тебя:\n👉 [{}]({})\n`Хорошего времяпровождения, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")
        
      


@borg.on(admin_cmd(pattern="dyno(.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://dashboard.heroku.com/account/{}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **Dyno** специально для тебя:\n👉 [{}]({})\n`Лови ссылку, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")
      
@borg.on(admin_cmd(pattern="lmgit(.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://github.com/search?q={}".format(input_str.replace(" ","+"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **GitHub** специально для тебя:\n👉 [{}]({})\n`Лови ссылку на репозиторий, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")

@borg.on(admin_cmd(pattern="lmw(.*)"))



async def _(event):



    if event.fwd_from:



        return



    input_str = event.pattern_match.group(1)



    sample_url = "https://da.gd/s?url=https://ru.wikipedia.org/wiki/{}".format(input_str.replace(" ","_"))



    response_api = requests.get(sample_url).text



    if response_api:



        await event.edit("Я проверю **Wikipedia** специально для тебя:\n👉 [{}]({})\n`Молодец, что решил узнать новое, не забудь сказать спасибо! 😉` ".format(input_str,response_api.rstrip()))



    else:



        await event.edit("Хьюстон, у нас проблемы! Попробуй позже.")
