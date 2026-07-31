import telebot
from flask import Flask
from threading import Thread
import os

# ضع توكن البوت الحقيقي هنا
TOKEN = "8631102007:AAGZ3ijUN945H6Xjnc2tLrLBd6CUzg0v-4o"

bot = telebot.TeleBot(TOKEN)
app = Flask(name)

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت يعمل بنجاح الآن على Render 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

if name == "main":
    keep_alive()
    print("البوت يعمل الآن...")
    bot.infinity_polling()
