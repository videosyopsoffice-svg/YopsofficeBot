import telebot
import os

TOKEN = os.getenv('TOKEN')

if not TOKEN:
    raise Exception("TOKEN manquant dans Railway")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bienvenue sur YopsOffice 🎬\n\nIci tu trouves tous les grands événements du cinéma.\n\nTape /films pour les films\nTape /series pour les séries")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Commandes dispos :\n/start - Accueil\n/films - Voir les films\n/series - Voir les séries")

@bot.message_handler(commands=['films'])
def films(message):
    bot.reply_to(message, "🎬 Liste des films à venir...\n\n1. Deadpool 3\n2. Dune 2\n\nBientôt plus de contenu !")

@bot.message_handler(commands=['series'])
def series(message):
    bot.reply_to(message, "📺 Liste des séries à venir...\n\n1. House of the Dragon S2\n2. The Boys S4\n\nBientôt plus de contenu !")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Tu as dit : {message.text}\nTape /help pour les commandes")

print("Bot YopsOffice démarré...")
bot.infinity_polling()
