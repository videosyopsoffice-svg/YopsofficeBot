import telebot
import os
from flask import Flask

app = Flask(__name__)
TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def home():
    return "Yopsoffice Bot en ligne H24"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Yopsoffice Bot est réveillé 🔥 Tape /help pour voir les commandes")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Commandes dispo :\n/start - Démarrer\n/help - Aide")

if __name__ == "__main__":
    from threading import Thread
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()
    bot.infinity_polling()
