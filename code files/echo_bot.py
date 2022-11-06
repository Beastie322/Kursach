#content_types=["text", "sticker", "pinned_message", "photo", "audio"] - пример типа сообщения
import time
import logging
from aiogram import Bot, Dispatcher, executor, types
import telebot
import commands

HIMSG = "Приветствуем, {}, в нашем боте для студентов ГУАП. Вы можете ознакомиться с командами, если напишите в чат /help."

bot = telebot.TeleBot("5735777277:AAEMCAbuXN8kMRuDJjlas9uCT1eAl4Kj4Vs")

logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    bot.send_message(user_id, HIMSG.format(user_name))

@bot.message_handler(commands=['help'])
def send_helping(message):
    user_id = message.from_user.id
    bot.send_message(user_id, commands.helping)


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.infinity_polling()