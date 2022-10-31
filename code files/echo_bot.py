#content_types=["text", "sticker", "pinned_message", "photo", "audio"] - пример типа сообщения

import telebot


bot = telebot.TeleBot("5735777277:AAEMCAbuXN8kMRuDJjlas9uCT1eAl4Kj4Vs")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()