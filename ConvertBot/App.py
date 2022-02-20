import telebot
from Config import exchanges, TOKEN
from Extensions import ConvertionException, CryptoConverter
from telebot import types


bot = telebot.TeleBot(TOKEN)


con_markup = types.ReplyKeyboardMarkup()
buttons = []
for values in exchanges.keys():
    buttons.append(types.KeyboardButton(values.capitalize()))
con_markup.add(*buttons)
    

@bot.message_handler(commands = ['start', 'help'])
def help(message : telebot.types.Message):
    text = 'To use bot write: <name of the currency being converted> <name of the currency in which you want to convert> <amount of the first currency> \n To see all values write /values'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ['values'])
def values(message : telebot.types.Message):
    text = 'Values:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types= ['text', ])
def convert(message : telebot.types.Message):
    try:
        values = message.text.split(' ')
        
        if len(values) != 3:
            raise ConvertionException('Too much arguments')

        base, quote, amount = values
        asked_cont = CryptoConverter.convert(base, quote, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Users error:\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Cant process command:\n{e}')

    else:
        text = f"Price of {amount} {base} in {quote} is {asked_cont}"
        bot.send_message(message.chat.id, text)


bot.polling()