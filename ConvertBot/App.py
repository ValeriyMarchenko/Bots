import telebot
from Config import exchanges, TOKEN
from Extensions import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)
    

@bot.message_handler(commands = ['start', 'help'])
def help(message : telebot.types.Message):
    text = 'To use bot write smthng like this: \n <value1> <value2> <value3> \n To see all values type /values'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ['values'])
def values(message : telebot.types.Message):
    text = 'Values:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types= ['text', ])
def convert(message : telebot.types.Message):
    values = message.text.split(' ')
    
    if len(values) != 3:
        raise ConvertionException('Too mach arguments')

    base, quote, amount = values
    asked_cont = CryptoConverter.convert(base, quote, amount)

    text = f"Price of {amount} {base} in {quote} is {asked_cont}"
    bot.send_message(message.chat.id, text)


bot.polling()