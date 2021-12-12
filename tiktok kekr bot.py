import telebot
import secrets
from telebot import types
bot = telebot.TeleBot("PUT TOKEN HERE")


@bot.message_handler(commands=['start'])
def all(massage):

	
	bot.reply_to(massage,text=f"<strong>🇺🇸 Welcome In This TikTok Checker ! 📡 </strong>\n Send [/run] To Start Checking <ins>(every run You make it will check 15 usernames every time ❗️) </ins>\n \n<strong>🇸🇦 اهلاً بك في تشيكر التيك توك ! 📡</strong>\n ارسل [/run] لبدأ الفحص <ins>(في كل مره تقوم انت بتشغيل الفحص سوف يتم فحص 15 يوزر في كل مره ❗️)</ins> \n \n -----------------------------------------------------------------------------\n \n<strong>Maybe The Users That is [AVAILABLE] will be [BANNED] (that's in every Checker) \n قد تكون اليوزرات [المتاحة] مبندة (هذا في كل فاحص) ⚒</strong> \n \n Me - @sMx_7d / My Channel  - @sMx7d 🔮💜",parse_mode='HTML')
	print(massage.chat.username)

	with open ('id.txt' , 'r+') as data:
		file = data.read()
		search = (str(massage.chat.id))
		if (str(search)) in file:
			print ('data exits!')
		else:
			data.write(str(massage.chat.id))
			data.write(str('\n'))
			data.close
			print('i got a new data!')

			with open ('user.txt','r+')as data2:
				data2.write(massage.chat.username)
				data2.write('\n')
				data2.close	

@bot.message_handler(commands=['run'])
def run(massage):
	bot.reply_to(massage,text='*🇺🇸 Start Checking 🚀! *\n   Let The Magic Happen 🪄 \n \n*🇸🇦 بدأ الفحص 🚀! *\n   دع السحر يحدث 🪄',parse_mode='markdown')

	for i in range(15):
		password_length = 3
		password = (secrets.token_urlsafe(password_length))
		import requests
		from os import system

		a = requests.Session()


		co = 0
		do = 0
		fa = 0


		url = f"https://www.tiktok.com/@{password}"

		head = {
	        'Host': 'www.tiktok.com',
	        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
	        "Accept-Language": "en-us",
	        "Accept-Encoding": "gzip, deflate, br",
	        'Connection': 'keep-alive'
	    }

		re = a.get(url, headers=head)
		if re.status_code == 404:
		    co += 1
		    do += 1
		    print(f"[+] Found >> {password} | Checked: {co}")
		    bot.reply_to(massage,text=f'*[{password}] IS AVAILABLE OR BANNED ✅*' ,parse_mode ='markdown')
		elif re.status_code == 200:
		    co += 1
		    fa += 1
		    print(f"[-] Taken >> {password} | Checked: {co}")

		    bot.reply_to(massage,text=f'*[{password}] IS NOT AVAILABLE ❌*' ,parse_mode ='markdown')

@bot.message_handler(commands=['admin'])
def admin(massage):
	if massage.chat.id == 723051294:
		with open('id.txt') as u:
			lineIDs = 0
			for line in u:
				lineIDs += 1
				lineID = (str(lineIDs))

		with open('user.txt') as l:
			line_lan = 0
			for line in l:
				line_lan += 1
				lineU = (str(line_lan))

		bot.reply_to(massage,f'Hi Dad! We Now Have Now {lineU} Users 🤖☄️ \n Hi Dad! We Now Have Now {lineID} Users 🤖☄️')

	else:
		bot.reply_to(massage,'sorry that not 4 u 🍫')

bot.infinity_polling()
