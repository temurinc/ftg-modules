"""Get details of a series or movie.
Command: 
.tv <название сериала>
.film <название фильма>
  © [cHAuHaN](http://t.me/amnd33p)"""

import requests
import bs4
import re
from telethon import *
from uniborg import *

@borg.on(events.NewMessage(outgoing=True,pattern='.film (.*)'))

@borg.on(events.MessageEdited(outgoing=True,pattern='.film (.*)'))

@borg.on(events.NewMessage(outgoing=True,pattern='.tv (.*)'))

@borg.on(events.MessageEdited(outgoing=True,pattern='.tv (.*)'))

async def imdb(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        try:
            movie_name = e.pattern_match.group(1)
            remove_space = movie_name.split(' ')
            final_name = '+'.join(remove_space)
            page = requests.get("https://www.imdb.com/find?ref_=nv_sr_fn&q="+final_name+"&s=all")
            lnk = str(page.status_code)
            soup = bs4.BeautifulSoup(page.content,'lxml')
            odds = soup.findAll("tr","odd")
            mov_title = odds[0].findNext('td').findNext('td').text
            mov_link = "http://www.imdb.com/"+odds[0].findNext('td').findNext('td').a['href']
            page1 = requests.get(mov_link)
            soup = bs4.BeautifulSoup(page1.content,'lxml')
            if soup.find('div','poster'):
              poster = soup.find('div','poster').img['src']
            else:
              poster = ''
            if soup.find('div','title_wrapper'):
              movie_title = soup.find('div','title_wrapper').findNext('h1').text
              pg = soup.find('div','title_wrapper').findNext('div').text
              mov_details = re.sub(r'\s+',' ',pg)
            else:
              mov_details = ''
            credits = soup.findAll('div', 'credit_summary_item')
            if len(credits)==1:
              director = credits[0].a.text
              writer = 'Недоступно :cry:'
              stars = 'Недоступно :cry:'
            elif len(credits)>2:
              director = credits[0].a.text
              writer = credits[1].a.text
              actors = []
              for x in credits[2].findAll('a'):
                actors.append(x.text)
              actors.pop()
              stars = actors[0]+','+actors[1]+','+actors[2]
            else:
              director = credits[0].a.text
              writer = 'Недоступно :cry:'
              actors = []
              for x in credits[1].findAll('a'):
                actors.append(x.text)
              actors.pop()
              stars = actors[0]+','+actors[1]+','+actors[2]
            if soup.find('div', "inline canwrap"):
              story_line = soup.find('div', "inline canwrap").findAll('p')[0].text
            else:
              story_line = 'Недоступно :cry:'
            info = soup.findAll('div', "txt-block")
            if info:
              mov_country = []
              mov_language = []
              for node in info:
                a = node.findAll('a')
                for i in a:
                  if "country_of_origin" in i['href']:
                    mov_country.append(i.text)
                  elif "primary_language" in i['href']:
                    mov_language.append(i.text)
            if soup.findAll('div',"ratingValue"):
              for r in soup.findAll('div',"ratingValue"):
                mov_rating = r.strong['title']
            else:
              mov_rating = 'Недоступно :cry:'
            await e.edit('<b>Название : </b><code>'+mov_title+
                  '<a href='+poster+'> ‏‏‎ </a>'
                  '</code>\n<code>'+mov_details+
                  '</code>\n<b>Оценки : </b><code>'+mov_rating+
                  '</code>\n<b>Страна : </b><code>'+mov_country[0]+
                  '</code>\n<b>Язык : </b><code>'+mov_language[0]+
                  '</code>\n<b>Режиссёр : </b><code>'+director+
                  '</code>\n<b>Сценарист : </b><code>'+writer+
                  '</code>\n<b>Звёзды : </b><code>'+stars+
                  '</code>\n<b>IMDB ссылка : </b>'+mov_link+
                  '\n\n<b>Держи пёселя : </b> <a href="https://www.unn.com.ua/uploads/assets/images/%D0%92%D0%B5%D0%BB%D1%8C%D1%88-%D0%BA%D0%BE%D1%80%D0%B3%D0%B8%20%D0%BF%D0%B5%D0%BC%D0%B1%D1%80%D0%BE%D0%BA.jpg">Пёсель</a>'+
                  '\n\n===> Приятного дня! <===',
                  link_preview = True , parse_mode = 'HTML'
                  )
        except IndexError:
            await e.edit("Хьюстон, результатов не найдено. Пожалуйста, введи ** Правильное название фильма / сериала **")
        except Exception as err:
            await e.edit("Хьюстон, произошла некая ошибка:- "+str(err))
