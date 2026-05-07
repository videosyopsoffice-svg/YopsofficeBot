import telebot
import os
from flask import Flask
from threading import Thread

app = Flask(__name__)

TOKEN = os.getenv('TOKEN')
PORT = int(os.getenv('PORT', 8080))

if not TOKEN:
    raise Exception("TOKEN manquant dans Railway Variables")

bot = telebot.TeleBot(TOKEN)

@app.route('/')
def home():
    return "Yopsoffice Bot en ligne H24"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Yopsoffice Bot est réveillé ✅")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Commandes disponibles: /start /help")

def run_flask():
    app.run(host='0.0.0.0', port=PORT)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    bot.infinity_polling()
