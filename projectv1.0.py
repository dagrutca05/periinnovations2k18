import telebot

TOKEN = '594167976:AAF_JFvTuN9cVL5g8kpDhJaGaIqn1ExcaRw'

bot = telebot.TeleBot(TOKEN)
			
# keyboard = telebot.types.ReplyMarkupKeyboard(resize_keyboard = True)
# keyboard.row('Экшн','Ужасы','Драма','Комедия')

@bot.message_handler(commands = ['start'])
def beginning(message):
	bot.send_message(message.chat.id, 'введите команду /getFilm чтобы заполнить анкету')

@bot.message_handler(commands = ['getFilm'])
def answer(message):
 line_kb = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру
 but_film = telebot.types.InlineKeyboardButton(text = 'Боевик',
	callback_data = 'Боевик') # создаем кнопку
 line_kb.add(but_film) # вешаем кнопку на клавиатуру

 but_kinopoisk = telebot.types.InlineKeyboardButton(text = 'Ужасы',
	callback_data = 'Ужасы') 
 line_kb.add(but_kinopoisk)
 but_serial = telebot.types.InlineKeyboardButton(text = 'Комедии',
	callback_data = 'Комедии')
 line_kb.add(but_serial)
 msg = bot.send_message(message.chat.id, 'Я тебе помогу определиться с выбором фильма. Ответь на несколько вопросов. \nВаш любимый жанр?', reply_markup = line_kb)


@bot.callback_query_handler(func = lambda call:True) 
def random_film(callobj):
	if callobj.data == 'Боевик':
		line_kb2 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk = telebot.types.InlineKeyboardButton(text = '<2000',
		 callback_data = '<2000') 
		line_kb2.add(but_poisk)
		but_serial2 = telebot.types.InlineKeyboardButton(text = '2000 - 2010',
		 callback_data = '2000 - 2010')
		line_kb2.add(but_serial2)
		but3_film = telebot.types.InlineKeyboardButton(text = '2011 - 2018',
		 callback_data = '2011 - 2018')
		line_kb2.add(but3_film)
		bot.send_message(callobj.message.chat.id, 'Фильм какого года ты хочешь увидеть?',reply_markup = line_kb2)


	if callobj.data == '<2000':
		line_kb4 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk4 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '<200012+') 
		line_kb4.add(but_poisk4)
		but_serial5 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '<200016+')
		line_kb4.add(but_serial5)
		but6_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '<200018+')
		line_kb4.add(but6_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb4)
		 
		
	elif callobj.data == '2000 - 2010':
		
		line_kb6 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk7 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '2000 - 201012+') 
		line_kb6.add(but_poisk7)
		but_serial7 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '2000 - 201016+')
		line_kb6.add(but_serial7)
		but9_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '2000 - 201018+')
		line_kb6.add(but9_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb6)

		 # if callobj.data == '12+':
		 #  bot.send_message(message.chat.id, 'Таинственный остров')
		 # elif callobj.data == '16+':
		 #  bot.send_message(message.chat.id, 'Пираты Карибского моря')
		 # elif callobj.data == '18+':
		 #  bot.send_message(message.chat.id, 'Убивая мертвецов')
		
	elif callobj.data == '2011 - 2018':
		
		line_kb10 = telebot.types.InlineKeyboardMarkup() # создаем клавиатуру 

		but_poisk10 = telebot.types.InlineKeyboardButton(text = '12+',
		 callback_data = '2011 - 201812+') 
		line_kb10.add(but_poisk10)
		but_serial10 = telebot.types.InlineKeyboardButton(text = '16+',
		 callback_data = '2011 - 201816+')
		line_kb10.add(but_serial10)
		but10_film = telebot.types.InlineKeyboardButton(text = '18+',
		 callback_data = '2011 - 201818+')
		line_kb10.add(but10_film)
		bot.send_message(callobj.message.chat.id, 'Фильм с какой возрастной категорией ты хочешь увидеть?',reply_markup = line_kb10)

	if '<2000' in callobj.data:
		if '12+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Люди Икс')
		elif '16+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Матрица')
		elif '18+' in callobj.data:
		 bot.send_message(callobj.message.chat.id, 'Фильм не найден')

	elif '2000 - 2010' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Таинственный Остров')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Пираты Карибского моря')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Убивая мертвецов')

	elif '2011 - 2018' in callobj.data:
		if '12+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Стражи Галактики')
		elif '16+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Риддик')
		elif '18+' in callobj.data:
			bot.send_message(callobj.message.chat.id, 'Расплата')


		 # if callobj.data == '12+':
		 #  bot.send_message(message.chat.id, 'Стражи Галактики')
		 # elif callobj.data == '16+':
		 #  bot.send_message(message.chat.id, 'Риддик')
		 # elif callobj.data == '18+':
		 #  bot.send_message(message.chat.id, 'Расплата')


if __name__ == '__main__':
 bot.polling()