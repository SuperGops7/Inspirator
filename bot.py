import telebot
from dotenv import dotenv_values

import quotes_getter 


BOT_TOKEN = dotenv_values('.env').get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['quote'])
def quote_handler(message):
    quote, author, error = quotes_getter.get_my_quote(category='inspirational')
    if error:
        send_text = error
    else:
        send_text = """{0}  
                    *{1}*""".format(quote, author)
    bot.send_message(message.chat.id, send_text, parse_mode="Markdown")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message)

bot.infinity_polling()

