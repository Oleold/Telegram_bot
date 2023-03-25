def main():
	import time
	import telebot
	from telebot import types
	import config
	import requests
	from translate import Translator
	import random

	bot = telebot.TeleBot("token")


	@bot.message_handler(commands=['start', 'help', 'random_cat', 'random_dog'])
	def send_welcome(message):
		if message.text == "/start":
			bot.reply_to(message, "Здравствуйте, {0.first_name}.Для продолжения введи число. Для краткой сводки введи: /help. \n Коты: /random_cat \n Собаки: /random_dog" .format(message.from_user))
		elif message.text == "/help":
			bot.reply_to(message, "Просто введи число, а я тебе факт про него")
		elif message.text == "/random_cat":
			source = requests.get(f"https://aws.random.cat/view/{random.randint(1, 1500)}").text
			sat = source.split("src=\"")[1].split("\"")[0]
			privet = ["Упс... Вот тебе кот", "Кота в студию"]
			bot.send_message(message.chat.id, privet[random.randint(0, 1)])
			bot.send_photo(message.chat.id, sat)
		elif message.text == "/random_dog":
			source = requests.get(f"https://random.dog/woof.json")
			s = source.json()["url"]
			privet = ["Упс... Вот тебе пёс", "Кто же это, ну ,конечно, эта - пёс"]
			bot.send_message(message.chat.id, privet[random.randint(0, 1)])
			bot.send_photo(message.chat.id, s)

	@bot.message_handler(content_types=['text'])
	def Name_print(message):
		try:
			t = message.text
			for i in range(len(t)):
				if not t[i].isdigit():
					b = 1 / 0
			response = requests.get('http://numbersapi.com/'+str(t))
			response.encoding = 'utf-8'
			trans = Translator(from_lang="en", to_lang="ru")
			text = response.text
			end_text = trans.translate(text)

			if end_text == str(t)+" - это число, для которого мы упускаем факт (отправьте его в numbersapi в google mail!).":
				bot.send_message(message.chat.id, "Не знаю фактов про это число.")
			else:
				bot.send_message(message.chat.id, end_text)

		except:
			if message.text=="Рандомная дата":
				response = requests.get('http://numbersapi.com/random/date')
				response.encoding = 'utf-8'
				trans = Translator(from_lang="en", to_lang="ru")
				text = response.text
				end_text = trans.translate(text)
				bot.send_message(message.chat.id, end_text)
			elif message.text=="Рандомная мелочь":
				response = requests.get('http://numbersapi.com/random/trivia')
				response.encoding = 'utf-8'
				trans = Translator(from_lang="en", to_lang="ru")
				text = response.text
				end_text = trans.translate(text)
				bot.send_message(message.chat.id, end_text)
			elif message.text=="Рандомный год":
				response = requests.get('http://numbersapi.com/random/year')
				response.encoding = 'utf-8'
				trans = Translator(from_lang="en", to_lang="ru")
				text = response.text
				end_text = trans.translate(text)
				bot.send_message(message.chat.id, end_text)
			elif message.text=="Рандомная математика":
				response = requests.get('http://numbersapi.com/random/math')
				response.encoding = 'utf-8'
				trans = Translator(from_lang="en", to_lang="ru")
				text = response.text
				end_text = trans.translate(text)
				bot.send_message(message.chat.id, end_text)
			else:
				bot.send_message(message.chat.id, "Упс... Это не число.")



	bot.infinity_polling()

if __name__ == '__main__':
	main()
