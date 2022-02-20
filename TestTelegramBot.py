import telebot

TOKEN = "5122604094:AAHkcbskE1FHt97EAsVSmSm9QZLAtiwMjZA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def welcome_msg(message):
    bot.send_message(message.chat.id, f'Welcome, {message.chat.username}')

@bot.message_handler(content_types = ['document', 'audio'])
def handle_docs_audio(message):
    pass

@bot.message_handler(content_types = ['photo'])
def handle_photo(message : telebot.types.Message):
    bot.reply_to(message, 'Nice meme bro')


bot.polling(none_stop = True) 
