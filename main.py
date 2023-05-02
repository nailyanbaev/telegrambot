import telebot

bot = telebot.TeleBot('5837141203:AAF129bldHWzILHiDBSThSTWpPNxnx39Z4k')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здарова бро))")

@bot.message_handler(commands=['че?'])
def che(message):
    bot.send_message(message.chat.id, "Все першке мээн, ты же меня знаешь бро))")

@bot.message_handler(commands=['бро'])
def bro(message):
    bot.send_message(message.chat.id, "Бро, нига, гангста щеет мэээн))")

@bot.message_handler(commands=['дерьмо'])
def bro(message):
    bot.send_message(message.chat.id, "Эй нига, ты где здесь дерьмо увидел??? Ну разок посрал в гараже, че теперь заебывать меня всю жизнь будешь??)")

@bot.message_handler(commands=['dj'])
def dj(message):
    bot.send_message(message.chat.id, "Бро, дай трэчок свести, ты же меня знаешь я не обосрусь))")

@bot.message_handler(commands=['костя'])
def kos(message):
    bot.send_message(message.chat.id, "Моя судьба тусить, бро, тебе меня не изменить))")

@bot.message_handler(commands=['оля'])
def olya(message):
    bot.send_message(message.chat.id, "Оля джан, я буду стоять рядом с тобой когда ты будешь играть и томно дышать на тебе перегаром))")

@bot.message_handler(commands=['женя'])
def zhenya(message):
    bot.send_message(message.chat.id, "Йо, ты спишь чтоли? Время то детское йопт макарек))")

@bot.message_handler(commands=['бля'])
def zhenya(message):
    bot.send_message(message.chat.id, "Йо мэээн, будь мужиком блиа! Андрей, давай кидай рыбу!!))")

bot.polling(none_stop=True)
