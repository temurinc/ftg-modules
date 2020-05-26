"""
Ищем торренты с сайта torrentdownloads.me
Команда: .tor search_string
Внимание: количество результатов я ограничил до 20

"""
from bs4 import BeautifulSoup as bs 
import requests
from telethon import events
from uniborg.util import admin_cmd
import asyncio
from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name='HumanX')


@borg.on(admin_cmd(pattern="tor ?(.*)", allow_sudo=True))
async def tor_search(event):
	if event.fwd_from:
		return 
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
# используем юзер-агента для корректной работы
	search_str = event.pattern_match.group(1)

	print(search_str)
	await event.edit("Ищу "+search_str+".....")
	if " " in search_str:
		search_str = search_str.replace(" ","+")
		print(search_str)
		res = requests.get("https://www.torrentdownloads.me/search/?new=1&s_cat=0&search="+search_str,headers)

	else:
		res = requests.get("https://www.torrentdownloads.me/search/?search="+search_str,headers)

	source = bs(res.text,'lxml')
	with open("source.html",'w') as f:
		f.write(str(source))

	urls = []
	magnets = []

	counter = 0
	for a in source.find_all('a',{'class':'cloud'}):
		# print("https://www.torrentdownloads.me"+a['href'])
		try:
			urls.append("https://www.torrentdownloads.me"+a['href'])
		except:
			pass
		if counter == 19:
			break		
		counter = counter + 1
	if not urls:
		await event.edit("Так, Роскомнадзор, я не понял - либо ключевое слово ограничено, либо не найдено ..")		
		return

	print("Ищу ссылку (в сибирь)")
		
	for url in urls:
		res = requests.get(url,headers)
		# print("URl: "+url)
		source = bs(res.text,'lxml')
		with open("source2.html",'w') as f:
			f.write(str(source))
		for div in source.find_all('div',{'class':'grey_bar1 back_none'}):
			try:
				mg = div.p.a['href']
				# print(str(mg)) потом попробую
				
   				sample_url = "https://da.gd/s?url={}.format(url)
				response_api = requests.get(sample_url).text
				magnets.append("<b>Ссылка: </b>"+str(response_api.rstrip())+"<br/><b>\nМагнет: </b>{}\n<br/>".format(str(mg)))
			except:
				pass	
	print("Ищу магнеты (нет, Эрик, я не про тебя)")			
	msg = ""
	try:
		search_str = search_str.replace("+"," ")
	except:
		pass	
	for i in magnets:
		msg = msg + i
	response = telegraph.create_page(
	search_str,
	html_content = msg
	)	
	await event.edit('Вот магнеты по {}:\nhttps://telegra.ph/{}'.format(search_str,response['path']))
