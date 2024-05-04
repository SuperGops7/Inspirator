import telebot
from dotenv import dotenv_values

import quotes_getter 


BOT_TOKEN = dotenv_values('.env').get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    bot.reply_to(message, "Type /quote to get started")

@bot.message_handler(commands=['quote'])
def quote_type_handler(message):
    send_text = "What type of quotes do you want? Choose one of the following\nInspirational\nFitness\nLeadership\nSuccess "
    sent_msg = bot.send_message(message.chat.id, send_text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, quote_sender)
    
def quote_sender(message):
    quote_type = message.text.lower()
    if quote_type not in ["inspirational", "fitness", "leadership", "success"]:
        bot.send_message(message.chat.id, "Invalid option, try again by giving \quote")
    else:
        quote, author, error = quotes_getter.get_my_quote(category=quote_type)
        if error:
            send_text = error
        else:
            send_text = """{0}  
                        *{1}*""".format(quote, author)
        bot.send_message(message.chat.id, send_text, parse_mode="Markdown")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.send_message(message.chat.id, "Invalid option, try again by giving /quote")

bot.infinity_polling()

