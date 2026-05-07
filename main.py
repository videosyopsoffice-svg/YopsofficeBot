import telebot
import os

TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise Exception("TOKEN manquant dans Railway")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Yopsoffice Bot en ligne H24 🔥")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Commandes disponibles : /start /help")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Tu as dit : {message.text}")

print("Bot démarré...")
bot.infinity_polling()
