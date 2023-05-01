import telebot

bot = telebot.TeleBot('5837141203:AAF129bldHWzILHiDBSThSTWpPNxnx39Z4k')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здарова братка))')


bot.polling(none_stop=True)
